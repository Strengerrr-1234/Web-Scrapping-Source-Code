import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "http://example.com/"

# Fetch the webpage content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract and print all headings (h1, h2, h3)
    print("Headings:")
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        print(heading.text.strip())
    
    # Extract and print all hyperlinks
    print("\nLinks:")
    for link in soup.find_all('a', href=True):
        print(f"{link.text.strip()}: {link['href']}")
    
    # Extract and print all paragraphs
    print("\nParagraphs:")
    for paragraph in soup.find_all('p'):
        print(paragraph.text.strip())
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
