from typing import List

from query_parameters import get_query_params
from urllib import response
import requests


class NumberGenerator:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        return requests.get(self.url, params=get_query_params())


class Computer:
    def __init__(self, value):
        self.value = value

    def computer_value(self):
        return self.value


def computer_guess() -> List[str]:
    website = "https://www.random.org/integers/"
    random_number = NumberGenerator(website).scrape()
    computer_number = random_number.text.split("\n")
    # ['4', '5', '4', '1', '']
    computer_number.pop()
    return Computer(computer_number).computer_value()

