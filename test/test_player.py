from io import StringIO
from typing import List
from unittest import mock

import pytest
from models import player_info

from models.player_info import game_players, get_player_info, player_guess


def test_game_player():
    computer = ['1', '2', '3', '4']
    player = ['2', '1', '7', '4']
    assert game_players(computer, player) == (3, 1)
