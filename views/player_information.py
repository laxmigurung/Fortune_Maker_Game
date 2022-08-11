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
