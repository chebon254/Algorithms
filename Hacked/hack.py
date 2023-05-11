import requests
from bs4 import BeautifulSoup

# The URL of the webpage you want to scrape
url = 'https://www.upwork.com/search/profiles/?q=Teresa%20Bell'

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element containing the bank card details, for example:
card_details_element = soup.find('div', {'class': 'card-details'})

# Extract the card number, CVV, and expiration date from the card details element, for example:
card_details_element = soup.find('div', {'class': 'payment-methods__form-row'})
card_number = None
cvv = None
expiration_date = None

if card_details_element is not None:
    card_number = card_details_element.find('input', {'name': 'card-number'}).get('value')
    cvv = card_details_element.find('input', {'name': 'cvv'}).get('value')
    expiration_date = card_details_element.find('input', {'name': 'expiration-date'}).get('value')



# Store the extracted data in a database or file, for example:
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object
c = conn.cursor()

if card_number is not None:
    c.execute("INSERT INTO card_details VALUES (?, ?, ?)", (card_number, cvv, expiration_date))



# Commit the transaction and close the connection
conn.commit()
conn.close()


# Print the extracted data
print("Card Number:", card_number)
print("CVV:", cvv)
print("Expiration Date:", expiration_date)