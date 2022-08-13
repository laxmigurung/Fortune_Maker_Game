from game_level import Level
from hint import level_hard_hint, level_medium_hint
from message import good_bye, welcome
from modify_tables import insert_player, insert_score_board
from player_info import player_guess, game_players, get_player_info

import number_generator
"""
easy_level, medium_level, hard_level: Created object of Level class with the instance attributes.

"""
easy_level = Level("easy", 0, 5, "1 million dollar", 1)
medium_level = Level("medium", 0, 5, "5 million dollar", 1)
hard_level = Level("hard", 0, 5, "10 million dollar", 1)

levels = [easy_level, medium_level, hard_level]


def start_game():
    welcome()
    player = get_player_info()
    insert_player(player[0], player[1])
    player_name = player[0]
    user_input = []

    for game in levels:
        print(f"Hi {player_name}, beginning {game.level} level.... ")
        print("********************************************")
        computer_number = number_generator.computer_guess()
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
        insert_score_board(game.level, game.points, game.prize_amount, )
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