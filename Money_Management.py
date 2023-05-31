import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://www.popsci.com/story/science/how-to-spend-money-happiness/"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Find all the article elements on the page
articles = soup.find_all("article")

# Iterate over each article and extract the title and link
for article in articles:
    # Extract the title
    title_element = article.find("h2")
    title = title_element.text.strip()
    
    # Extract the link
    link_element = article.find("a")
    link = link_element["href"]
    
    # Print the title and link
    print("Title:", title)
    print("Link:", link)
    print()