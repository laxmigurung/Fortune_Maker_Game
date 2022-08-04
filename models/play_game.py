from rand_int_api import computer_guess
from user_guess import guess_number


def my_func(computer, player):
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

    return counting_number, counting_position


attempts = 10
guess = False

while guess is False and attempts != 0:  # user gets 10 attempts to guess the number

    count_numbers, count_position = my_func(computer_guess(), guess_number())
    print("numbers: ", count_numbers, "position: ", count_position)
    if count_numbers == 4 and count_position == 4:
        guess = True
    else:
        attempts -= 1
        print("Attempt Left: ", attempts)
        guess = False
