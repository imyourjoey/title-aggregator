import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    # Replace the URL with the actual URL of the website you want to scrape
    url = "https://wired.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = []

        # Find all elements with the specified class containing the headlines
        for headline_elem in soup.find_all(class_='summary-item__content'):
            # Extract the title and link from the anchor tag within the container div
            link_elem = headline_elem.find('a', class_='summary-item__hed-link')
            title_elem = headline_elem.find('h2', class_='summary-item__hed')

            if link_elem and title_elem:
                # Extract title text and URL
                title = title_elem.text.strip()
                link = link_elem['href']

                full_url = url + link
                headlines.append({'title': title, 'url': full_url})

        return headlines
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Uncomment the line below for testing the scraper independently
# print(scrape_headlines())
