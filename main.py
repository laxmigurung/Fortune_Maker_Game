from typing import List

from database.insert_table import insert_player
from models.game import start_game
from views.player import get_player_info


player = get_player_info()
insert_player(player[0], player[1])
player_name = player[0]


