from unittest.mock import patch

import pytest

from models.play_game import game_hint


@pytest.mark.parametrize("[test_input, level, hint_list],expected",
                         [([['1', '6', '2', '7'], 'land', [0, 1, 2, 3]], ['1', '2', '6', '7'])])
def test_game_hint(test_input, expected):
    assert game_hint(test_input, level='land', hint_list=[0, 1, 2, 3]) == expected
