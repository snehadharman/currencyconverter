# Currency Converter

This is a simple Python program that allows you to convert currency between various international currencies using real-time exchange rates from the [Frankfurter API]. The program also shows the conversion rates for the past 5 days and saves all conversions in a local SQLite database for future reference.

## Features

- **Real-time Currency Conversion**: Get the latest exchange rates for currency conversion between different countries.
- **Past 5-Day Exchange Rates**: See historical exchange rates for the last 5 days.
- **Local Database Storage**: All conversions are stored in a local SQLite database, enabling you to view your past conversion history.
- **Terminal-Based**: A simple terminal-based interface, ideal for quick currency conversions.
  
### Requirements

To run this project, you will need:

- **Python 3.11.6**: Make sure you have Python installed on your machine. 
- **Internet Connection**: Required to fetch real-time exchange rates from the Frankfurter API.
- **Required Packages**: You need to install the `requests` package for making HTTP requests.

# Installation

## Step 1: Clone the Repository

To download the project, open a terminal and run the following command to clone the repository:

**Clone the repository:**
  
   git clone <repository-url>

**Install required packages:** 
  In your terminal, navigate to the project directory and run the following command to install the necessary Python packages:

  pip install requests

## How to Run
-In your terminal, navigate to the project folder.
-Run the program using the following command:

  python currency_converter.py

# Example Conversion Flow
Currency Conversion:

-The program will ask you to enter:
-The currency you want to convert from (e.g., USD).
-The currency you want to convert to (e.g., EUR).
-The amount you want to convert.
-It will fetch the latest exchange rate and show the converted amount.
-Additionally, the program will display conversion rates for the last 5 days.

View Conversion History:

-Choose this option to view a list of all your previous conversions. These are saved in a local SQLite database.

## How It Works
-Frankfurter API:  This API provides real-time and historical exchange rates for currency conversion. No API key is needed to use it.
-SQLite Database: The program stores each conversion, allowing you to view your past conversions in future runs.

### References
-Frankfurter API
-Python SQLite Documentation
-Requests Library

