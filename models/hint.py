import random


def level_medium_hint(computer_number):
    if random.randint(1, 3) == 1:
        computer_number.sort()
        print("Sorted the computer number for you. ;)")
        print(computer_number)

    else:
        print(f"Computer: __ {computer_number[1]} __ {computer_number[3]}")


def level_hard_hint(computer_number):
    if random.randint(1, 2) == 1:
        position = random.randint(0, 3)
        hint_number = computer_number[position]
        print(f"Position {computer_number.index(hint_number) + 1} has :  {hint_number} number")
    else:
        position = random.randint(0, 3)
        hint_number = computer_number[position]
        if int(hint_number) % 2 == 0:
            print(f"{computer_number.index(hint_number) + 1} : This position contains an even number.")
        else:
            print(f"{computer_number.index(hint_number) + 1} : This position contains an odd number.")
