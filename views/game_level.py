import NumberGenerator
from message import good_bye, welcome, winner
from player_information import player_guess, game_players
import random

class Level:
    def __init__(self, points, attempts, prize_amount, guess,total_hint):
        self.points = points
        self.attempts = attempts
        self.prize_amount = prize_amount
        self.guess = False
        self.total_hint = total_hint

    def hint(self):
        self.total_hint = self.total_hint - 1
        return self.total_hint


easy_level = Level(0, 5, "1 million dollar", False, 3)
medium_level = Level(0, 5, "5 million dollar", False, 3)
hard_level = Level(0, 5, "10 million dollar", False, 3)
final_level = Level(0, 5, "15 million dollar", False, 3)


def level_easy():

    welcome()
    computer_number = NumberGenerator.computer_guess()
    print(computer_number)
    for game in range(5):
        ask_help(computer_number)
        player_number = player_guess()
        count_numbers, count_position = game_players(computer_number, player_number)
        print("********************************************")
        print("Correct Numbers: ", count_numbers, "Correct Position: ", count_position)
        print("*******************************************")
        print(f"You have {easy_level.total_hint} hint available.")
        print("*******************************************")

        easy_level.attempts -= 1

        print("********************************************")
        if (count_numbers == 1 or 2 or 3 or 4) and count_position == 4:
            easy_level.points += 1
            print(f"Your Points: {easy_level.points}")
            print("Attempt Left: ", easy_level.attempts)
            print("********************************************")

            if easy_level.points == 3:
                print("Congratulations! You have 3 points. You can now move to medium level.")
                play_next_level = input("Do you want to play next level? (y for YES | press anything for NO):")
                if play_next_level == 'y':
                    easy_level.level_medium(easy_level.points)
                    break
                else:
                    print(f"You won {easy_level.prize_amount}.")
                    good_bye()
                    print(f"Your total Points: {easy_level.points}")
                    return easy_level.points
                    break
            else:
                computer_number = NumberGenerator.computer_guess()
                print(computer_number)
        else:
            print("Attempt Left: ", easy_level.attempts)
            continue
    else:
        print(f"Your Points: {easy_level.points}")
        print("Attempt Left: ", easy_level.attempts)
        print("Sorry you lost! ")
        good_bye()

def level_easy_hint(computer_number):
    print(f"Computer: __ {computer_number[1]} __ {computer_number[3]}")

def ask_help(computer_number):
    count_hint = 0
    if easy_level.total_hint > 0:
        ask_help = input('Do you need hint? (y for YES | press anything for NO): ')
        print("********************************************")
        if ask_help == "y":
            count_hint += 1
            easy_level.hint()
            level_easy_hint(computer_number)

    else:
        print("You have used all three help. No more help, sorry!")
level_easy()