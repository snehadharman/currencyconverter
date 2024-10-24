import requests
import sqlite3
from datetime import datetime, timedelta

# Connect to  database ( create it if it doesn't exist)
conn = sqlite3.connect('currency_history.db')
c = conn.cursor()

# Create a table to store conversion history (if it doesn't exist already)
c.execute('''CREATE TABLE IF NOT EXISTS conversion_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                from_currency TEXT,
                to_currency TEXT,
                amount REAL,
                converted REAL
            )''')
conn.commit()  # Save changes


# Function to get currency data for a specific date
def get_currency_data(date, from_currency, to_currency, amount):
    # Call the API with the given parameters
    url = f"https://api.frankfurter.app/{date}?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)

    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()       # Get  response data in JSON format
        if to_currency in data['rates']:
            return data['rates'][to_currency]      # Return the conversion rate
        else:
            print(f"Invalid currency: {to_currency}")
            return None
    else:
        print(f"Error fetching data for {date}")
        return None


# Function to save conversion record in the database
def save_conversion_to_db(date, from_currency, to_currency, amount, converted):
    # Insert the conversion data into the database
    c.execute('''INSERT INTO conversion_history (date, from_currency, to_currency, amount, converted)
                 VALUES (?, ?, ?, ?, ?)''', (date, from_currency, to_currency, amount, converted))
    conn.commit()  # Save the changes


# Function to show the conversion history
def show_conversion_history():
    c.execute('SELECT * FROM conversion_history')
    records = c.fetchall()  # Fetch all records from the table

    # If there are records, display them
    if records:
        print("\nConversion History:")
        for record in records:
            print(f"Date: {record[1]}, {record[3]} {record[2]} = {record[5]:.2f} {record[4]}")
    else:
        print("\nNo conversion history found.")


# Main function to run the script
def main():
    print("Welcome to the Currency Converter!")
    print("1. Convert currency")
    print("2. View conversion history")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Get input from the user
        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the destination currency (e.g., EUR): ").upper()

        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            return

        # Get conversion rates for the last 5 days
        today = datetime.now()
        for i in range(5):
            date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
            converted = get_currency_data(date, from_currency, to_currency, amount)

            if converted is not None:
                print(f"On {date}, {amount} {from_currency} = {converted:.2f} {to_currency}")
                 # Save the conversion data in the database
                save_conversion_to_db(date, from_currency, to_currency, amount, converted)
            else:
                print(f"Conversion failed for {date}.")

    elif choice == '2':
        show_conversion_history()       # Show  conversion history

    else:
        print("Invalid choice! Please enter 1 or 2.")


if __name__ == '__main__':
    main()


conn.close()   #close db
