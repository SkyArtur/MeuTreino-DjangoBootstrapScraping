import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url: str) -> None:
        self.__url = url

    @property
    def scraping_text_in_p_tag(self) -> list:
        response = requests.get(self.__url)
        html = BeautifulSoup(response.text, 'html.parser')
        return [link.get_text().strip() for link in html.find_all('p')]
