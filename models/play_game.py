from colorama import Fore

from datetime import datetime
from message import good_bye, welcome
from modify_tables import insert_player, insert_score_board
from player_info import player_guess, game_players, get_player_info

import number_generator
import random


class Level:
    def __init__(self, level, points, attempts, prize_amount, total_hint):
        self.level = level
        self.points = points
        self.attempts = attempts
        self.prize_amount = prize_amount
        self.total_hint = total_hint


"""
- Created two objects and assigned attributes value of th Level Class.
- Stored them in a list to perform FOR loop to run the game.
"""

land_level = Level("land", 0, 5, "1 million dollar", 2)
sky_level = Level("sky", 0, 8, "5 million dollar", 4)

levels = [land_level, sky_level]

"""
- get_game_info() function collects the information of user before starting the game.
    : param player: List prompts user to input username and email.
    : param player_name, player_email: stores the value from the list into the variables.
- insert_player() stores the player information into "player" table in FortuneMakerGame database.
- start_game() takes two arguments to display them during the game run.
"""


def get_game_info():
    welcome()
    player = get_player_info()
    player_name, player_email = player[0], player[1]
    date_start = datetime.now()
    #insert_player(player_name, player_email, date_start)
    start_game(player_name, date_start)


"""
function start_game(): main game run in this function.
:params user_input: List  - to store the user input numbers during the game, inorder for user to see the history.
:params computer_number: List  - this stores the computer generated number from the api call.
:params player_number: List - this stores the user input number.
"""


def start_game(player_name, date_start):
    total_points = 0
    user_input = []

    # Performed FOR loop to begin the game from LAND level to SKY level.
    for game in levels:
        guess = False
        print(Fore.LIGHTGREEN_EX + f"Hi {player_name}, beginning {game.level} level.... ")
        print(Fore.CYAN + "********************************************")
        print(f"Time: {date_start}")
        print(Fore.CYAN + "********************************************")
        print(f"You have {game.attempts} attempts and {game.total_hint} hint available for {game.level} level.")

        computer_number = number_generator.computer_guess()
        print(computer_number)
        player_number = player_guess()

        user_input.append(player_number)
        game.attempts -= 1
        count_numbers, count_position = game_players(computer_number, player_number)
        print(Fore.LIGHTRED_EX + f"Correct Numbers:  {count_numbers} Correct Position: {count_position}")
        if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
            print(f"Congratulations!! You completed level {game.level}")
            print(f"Hurray!! You won {game.prize_amount}")
            user_input.clear()
            continue
            if game.level == 'sky':
                good_bye()
                exit()

        print(f"Attempt Left: {game.attempts}")
        print(Fore.GREEN + "********************************************")
        print("YOU ENTERED")
        print_user_input(user_input)

        hint_list = [0, 1, 2, 3]

        while guess is False and game.attempts != 0:
            if game.total_hint > 0:
                ask_help = input(Fore.GREEN + "Do you need hint? Type 'y' for YES || type anything for NO ::  ")
                print(Fore.YELLOW + f"Hint Available Before hint: {game.total_hint}")
                if ask_help == 'y':
                    game.total_hint -= 1
                    game_hint(computer_number, game.level, hint_list)
                    print(Fore.YELLOW + f"Hint Available: {game.total_hint}")
            elif game.total_hint == 0:
                print(Fore.YELLOW + "No Hint Available")

            elif game.attempts == 0:
                print("You Lost")
                good_bye()
                exit()
            print(Fore.RED + f"Attempt Left: {game.attempts}")
            print(Fore.BLUE + "Guess again.....")
            player_number = player_guess()
            user_input.append(player_number)
            count_numbers, count_position = game_players(computer_number, player_number)
            print(Fore.GREEN + "********************************************")
            print(Fore.YELLOW + f"Correct Numbers:  {count_numbers} Correct Position: {count_position}")
            if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
                print(f"Congratulations!! You completed level {game.level}")
                print(f"Hurray!! You won {game.prize_amount}")
                user_input.clear()
                if game.level == 'sky':
                    good_bye()
                    exit()
                else:
                    guess = True
            game.attempts -= 1
            print(Fore.RED + f"Attempt Left: {game.attempts}")
            print(Fore.GREEN + "********************************************")
            print("YOU ENTERED")
            print_user_input(user_input)
            print(Fore.GREEN + "********************************************")
            """if game.attempts == 0:
                print("You Lost")
                good_bye()
                exit()"""
            compare(player_number, computer_number, game.points, game.prize_amount)
            total_points += 1
        else:
            print("I am here")

            # insert_score_board(1, 1, game.level, game.points, game.prize_amount, date_start)


# Comparing player's guess to computer number,if this is true, it will take you to next SKY level. If false,
# Performed while loop to let player guess the number,until it matches with computer or no attempts left.
def compare(player_num, comp_num, points, amount):
    if player_num == comp_num:
        print(Fore.BLUE + f"Congratulations! You won {amount}.")
        points += 1
        print(Fore.YELLOW + f"Your points: {points}")


def game_hint(computer_number, level, hint_list):
    if level == "land":
        position = random.choice(hint_list)
        hint_number = computer_number[position]
        print(Fore.YELLOW + f"{computer_number.index(hint_number) + 1} : This position contains {hint_number}.")
        hint_list.remove(position)

    else:
        position = random.choice(hint_list)
        hint_number = computer_number[position]
        if int(hint_number) % 2 == 0:
            print(
                Fore.LIGHTMAGENTA_EX + f"{computer_number.index(hint_number) + 1} : This position contains an even number.")
            hint_list.remove(position)
        else:
            print(
                Fore.LIGHTMAGENTA_EX + f"{computer_number.index(hint_number) + 1} : This position contains an odd number.")
            hint_list.remove(position)


# This function helps to store the user input history is clear format.
def print_user_input(user_input):
    for i in range(len(user_input)):
        for j in user_input[i]:
            print(Fore.RED + j, end=" ")
        print()


# This function call starts the game
get_game_info()
