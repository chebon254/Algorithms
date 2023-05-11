import requests
from bs4 import BeautifulSoup

# Fetch the webpage HTML code
response = requests.get('https://example.com')
html_code = response.content

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Find the div tag with class "nv-24"
nv24_div = soup.find('div', {'class': 'nv-24'})

# Extract the contents of the div tag
nv24_content = nv24_div.text
print(nv24_content)
