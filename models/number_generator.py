from log import log_error
from typing import List

import requests

"""This file contains all the required functions to generate the computer number from the website 
"https://www.random.org/integers/" .

"""

class QueryParameters:
    def __init__(self, num, min, max, col, base, format, rnd):
        self.num, self.min, self.max, self.col, self.base, self.format, self.rnd = num, min, max, col, base, format, rnd

    def get_query_params(self):
        query_params = {
            'num': self.num,
            'min': self.min,
            'max': self.max,
            'col': self.col,
            'base': self.base,
            'format': self.format,
            'rnd': self.rnd
        }
        return query_params


parameters = QueryParameters(4, 0, 7, 1, 10, 'plain', 'rnd')


class NumberGenerator:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        return requests.get(self.url, params=parameters.get_query_params())


class Computer:
    def __init__(self, value):
        self.value = value

    def computer_value(self):
        return self.value


"""
: params website: contains the url that generates the computer number for the game.
: params random_number: stores the random generated number
"""


def computer_guess() -> List[str]:
    try:
        website = "https://www.random.org/integers/"

        random_number = NumberGenerator(website).scrape()
        computer_number = random_number.text.split("\n")
        computer_number.pop()
        return Computer(computer_number).computer_value()

    except requests.exceptions.RequestException as e:
        log_error().warning(e)
