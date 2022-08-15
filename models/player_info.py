from colorama import Fore
from typing import List, Tuple


class PlayerInformation:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_player_info(self):
        return self.username, self.email


"""
This function prompts user to input username and email to store the data in the database.
"""


def get_player_info():
    username = input(Fore.BLUE + "Enter username: ")
    email = input(Fore.GREEN + "Enter your email: ")

    player_data = PlayerInformation(username, email)
    return list(player_data.display_player_info())


"""
This function game_players() gets the player and computer's number.
It checks the number of repetition of user input by comparing with the comuter number.

"""


def game_players(computer, player) -> Tuple[int, int]:
    counting_number = 0
    counting_position = 0
    matches = []
    hint = dict()
    hint["Position"] = "Value"

    for i in range(4):
        if player[i] not in matches:
            if player[i] == computer[i]:
                counting_position += 1
                counting_number += 1
                matches.append(player[i])
                hint[player.index(computer[i]) + 1] = player[i]

            elif player[i] in computer:
                counting_number += 1
                matches.append(player[i])

        elif player[i] in matches:
            if player[i] == computer[i]:
                counting_position += 1
                counting_number += 1

            elif player[i] in computer:
                counting_number += 1

    print(Fore.CYAN + "********************************************")
    print(Fore.BLUE + f"RESULT : {hint}")
    return counting_number, counting_position


"""
This functions prompts the player to input the four number combinations.
Following all the requirements, player must only input number between 0 to 7.
"""


def player_guess() -> List[str]:
    flag = True
    user_input = []
    index = 0
    while flag is True:
        try:
            print(Fore.CYAN + "----------------------------------------")
            number = int(input(Fore.LIGHTBLUE_EX + f"\tEnter a number between 0 to 7 in position {index + 1}:     "))
            if number < 0 or number > 7:
                print(Fore.GREEN + "You must enter number from 0 to 7 only!")
            else:
                user_input.append(str(number))
                index += 1
                if len(user_input) == 4:
                    flag = False
        except ValueError:
            print(Fore.LIGHTCYAN_EX + "No letters, symbols. Enter only numbers between 0 to 7!")
    return user_input
