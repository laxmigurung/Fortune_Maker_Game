from typing import List

from hint import level_hard_hint, level_medium_hint

from views.game_level import Level
from views.message import good_bye, welcome, winner
from views.player import player_guess, game_players
from views.number_generator import NumberGenerator

import random

"""
easy_level, medium_level, hard_level: Created object of Level class with the instance attributes.

"""
easy_level = Level("easy", 0, 5, "1 million dollar", 1)
medium_level = Level("medium", 0, 5, "5 million dollar", 1)
hard_level = Level("hard", 0, 5, "10 million dollar", 1)

levels = [easy_level, medium_level, hard_level]


def start_game():
    welcome()
    for game in levels:
        print(f"Beginning {game.level} level.... ")
        print("********************************************")
        computer_number = NumberGenerator.computer_guess()
        print(computer_number)
        player_number = player_guess()
        game.attempts -= 1
        count_numbers, count_position = game_players(computer_number, player_number)
        print(f"Correct Numbers:  {count_numbers} Correct Position: {count_position}")
        if player_number == computer_number:
            print("Congratulations! Proceeding to next level")
            game.points += 1
            print(f"You points: {game.points}")
            continue
        else:
            for i in range(game.attempts):
                print("Guess again: ")
                player_number = player_guess()
                count_numbers, count_position = game_players(computer_number, player_number)
                print(f"Correct Numbers:  {count_numbers} Correct Position: {count_position}")

                if player_number == computer_number:
                    print("Congratulations, you won easy level! Now let's play medium level.")
                    game.points += 1
                    print(f"You points: {game.points}")
                    continue
                else:
                    print(player_number)
                    continue
    else:
        good_bye()


def ask_help(computer_number, total_hint, level):
    if total_hint > 0:
        total_hint -= 1
        print(f"Hint Available: {total_hint} ")
        print("********************************************")
        if level == 'medium':
            level_medium_hint(computer_number)
        else:
            level_hard_hint(computer_number)
        return total_hint

    else:
        print("You have used all three help. No more help, sorry!")


start_game()
