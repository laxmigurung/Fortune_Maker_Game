from typing import List

from database.insert_table import insert_player
from views.game_level import Game
from views.player_information import get_player_info


'''player = get_player_info()
insert_player(player[0], player[1])
player_name = player[0]'''


def start_game():
    new_game = Game()
    new_game.level_easy()


start_game()
