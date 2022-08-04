from bs4 import BeautifulSoup
from query_parameters import query_params
from urllib import response
import requests


class Scrapper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        return requests.get(self.url, params=query_params)


def computer_guess() -> str:
    website = "https://www.random.org/integers/"
    random_number = Scrapper(website).scrape()
    return random_number.text


