"""from unittest import mock
from unittest.mock import patch

import pytest

from models.hint import level_easy_hint, level_hard_hint, level_medium_hint


@patch('builtins.print')
def test_level_easy_hint(mock_print):
    level_easy_hint(['1', '6', '2', '7'])
    mock_print.assert_called_with("Computer: __ 6 __ 7")


@pytest.mark.parametrize("test_input,expected",
                         [(['1', '6', '2', '7'], ['1', '2', '6', '7'])])
def test_level_medium_hint(test_input, expected):
    assert level_medium_hint(test_input) == expected


def test_level_hard_hint():
    pass"""
