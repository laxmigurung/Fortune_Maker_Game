from views import NumberGenerator
from database.insert_table import player_guess
from main import good_bye, welcome, winner
import random


def level_easy_hint(computer_number):
    print(f"Computer: __ {computer_number[1]} __ {computer_number[3]}")


def level_medium_hint(computer_number):
    position = random.randint(0, 3)
    hint_number = computer_number[position]
    print(f"Position {computer_number.index(hint_number) + 1} has :  {hint_number} number")


def level_hard_hint(computer_number):
    position = random.randint(0, 3)
    hint_number = computer_number[position]
    if int(hint_number) % 2 == 0:
        print(f"{computer_number.index(hint_number) + 1} : This position contains an even number.")
    else:
        print(f"{computer_number.index(hint_number) + 1} : This position contains an odd number.")


class Game:
    def level_easy(self) -> int:
        guess = False
        attempts = 10
        points = 0
        count_help = 0
        total_help = 3

        welcome()

        for game_run in range(10):
            computer_number = NumberGenerator.computer_guess()
            print(computer_number)
            if total_help > 0:
                ask_help = input('Do you need help? (y for YES | press anything for NO): ')
                if ask_help == "y":
                    count_help += 1
                    total_help -= 1
                    level_easy_hint(computer_number)

            else:
                print("You have used all three help. No more help, sorry!")

            print(f"You have {total_help} help left")
            player_number = player_guess()
            count_numbers, count_position = game_players(computer_number, player_number)
            print("numbers: ", count_numbers, "position: ", count_position)

            attempts -= 1

            if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
                points += 1
                print(f"Your Points: {points}")
                print("Attempt Left: ", attempts)
                if points == 5:
                    print("Congratulations! You have 5 points. You can now move to medium level.")
                    play_next_level = input("Do you want to play next level? (y for YES | press anything for NO):")
                    if play_next_level == 'y':
                        self.level_medium(points)
                    else:
                        print("You won 5 million dollars.")
                        good_bye()
                        print(f"Total Points: {points}")
                        return points
        else:
            print("Sorry you lost! ")
            good_bye()

    def level_medium(self, points) -> int:
        guess = False
        attempts = 5
        count_help = 0
        total_help = 3

        welcome()

        while guess is False and attempts != 0:
            computer_number = NumberGenerator.computer_guess()
            print(computer_number)

            if total_help > 0:
                ask_help = input('Do you need help? (y for YES | press anything for NO): ')
                if ask_help == "y":
                    count_help += 1
                    total_help -= 1
                    level_medium_hint(computer_number)

                else:
                    print("You have used all three help. No more help, sorry!")

            print(f"You have {total_help} help left")
            player_number = player_guess()
            count_numbers, count_position = game_players(computer_number, player_number)
            print("numbers: ", count_numbers, "position: ", count_position)
            attempts -= 1
            if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
                points += 1
                print(f"Your Points: {points}")
                if points == 10:
                    print("Congratulations! You have 10 points. You can now move to final level.")
                    play_next_level = input("Do you want to play next level? (y for YES | press anything for NO):")
                    if play_next_level == 'y':
                        self.level_hard(points)
                    else:
                        print(f"Total Points: {points}")
                        print("You won 10 million dollars.")
                        good_bye()
                        return points
                        guess = True
            else:
                print("Sorry you lost this round, but you still have $5 million! Congratulations!! ")
                good_bye()
                guess = True

    def level_hard(self, points):
        guess = False
        attempts = 5
        count_help = 0
        total_help = 5

        welcome()

        while guess is False and attempts != 0:  # user gets 10 attempts to guess the number
            computer_number = NumberGenerator.computer_guess()
            print(computer_number)

            if total_help > 0:
                ask_help = input('Do you need help? (y for YES | press anything for NO): ')
                if ask_help == "y":
                    count_help += 1
                    total_help -= 1
                    level_hard_hint(computer_number)

                else:
                    print("You have used all three help. No more help, sorry!")

            print(f"You have {total_help} help left")
            player_number = player_guess()
            count_numbers, count_position = game_players(computer_number, player_number)
            print("numbers: ", count_numbers, "position: ", count_position)
            attempts -= 1
            if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
                points += 1
                print(f"Your Points: {points}")
                if points == 15:
                    winner()
                    return points
                    guess = True
            else:
                print("Sorry you lost this round, but you still have $10 million! Congratulations!! ")
                good_bye()
                guess = True


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
