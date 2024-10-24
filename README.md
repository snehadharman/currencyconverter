# currencyconverter
This is a simple program that lets you convert money from one currency to another. It uses an online service called the Frankfurter API to get the latest exchange rates. The program can also show you conversion rates for the last 5 days and saves your past conversions in a small local database.

#What You Need to Run It
Python 3 (make sure you have it installed)
Internet connection (for fetching exchange rates)

#Download the project by cloning the repository:

#Install the required packages: You’ll need the requests package. Run this in your terminal:
pip install requests

#Run the program: In your terminal, type:

python currency_converter.py

Follow the instructions:

You can choose to either convert currency or view your conversion history.
For converting, enter the currencies and amount when prompted.
How It Works
The program will ask you to enter:
The currency you’re converting from (e.g., USD for US Dollars).
The currency you’re converting to (e.g., EUR for Euros).
The amount you want to convert.
The program will show you the conversion rates for the last 5 days.

It will also save the conversions so you can view them later.

How to View Conversion History
If you select the "View History" choice, you can see all your past conversions, which are stored in a local database.

This program is designed to be run in the terminal. 
It uses the Frankfurter API, but you don’t need an API key—just run the program.

References
Frankfurter API
Python SQLite Documentation

