import requests
from bs4 import BeautifulSoup


def scraper(url: str) -> list:
    context = list()
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    for link in html.find_all('p'):
        context.append(link.get_text().strip())
    return context
