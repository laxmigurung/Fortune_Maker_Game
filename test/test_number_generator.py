from unittest import mock

from models.number_generator import computer_guess, NumberGenerator


def test_computer_guess():
    assert type(computer_guess()) is list
    assert len(computer_guess()) == 4


def test_scrape():
    url = "https://www.random.org/integers/"
    assert NumberGenerator(url).scrape().status_code == 200


