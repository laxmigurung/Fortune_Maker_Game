from typing import List


class PlayerInformation:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_player_info(self):
        return self.username, self.email


def get_player_info():
    username = input("Enter username: ")
    email = input("Enter your email: ")

    player_data = PlayerInformation(username, email)
    return list(player_data.display_player_info())


def game_players(computer, player):
    counting_number = 0
    counting_position = 0
    matches = []
    for i in range(4):
        if player[i] not in matches:
            if player[i] == computer[i]:
                counting_position += 1
                counting_number += 1
                matches.append(player[i])
            elif player[i] in computer:
                counting_number += 1
                matches.append(player[i])
        elif player[i] in matches:
            counting_position += 1
            if player == computer:
                matches.append(player[i])

    return counting_number, counting_position


def player_guess() -> List[str]:
    try:
        flag = True
        user_input = []
        while flag is True:
            try:
                i = int(input("Enter Number:"))
                if i < 0 or i > 7:
                    print("You must enter number from 0 to 7 only")
                else:
                    user_input.append(str(i))
                    if len(user_input) == 4:
                        flag = False
            except ValueError:
                print("No letters,symbols.Enter only numbers between 0 to 7.")
        return user_input
    except ValueError:
        pass

for i in range(4):
    player_guess_number = int(input(f"Enter Number {enumerate(i)}:"))