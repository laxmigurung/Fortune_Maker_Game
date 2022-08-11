from database.dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error

from typing import List


def insert_player(username, email):
    insert_query = "INSERT INTO player(username, email) VALUES(%s, %s)"
    args = (username, email)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        curser = conn.cursor()
        curser.execute(insert_query, args)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        curser.close()
        conn.close()


def insert_score_board(player_id, level, points, prize_amount, date_time):
    insert_query = "INSERT INTO score_board(player_id, level, points, prize_amount, date_time) VALUES(%d, %d, %d, %d, " \
                   "%r) "
    args = (player_id, level, points, prize_amount, date_time)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        curser = conn.cursor()
        curser.execute(insert_query, args)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        curser.close()
        conn.close()


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
        get_user_input(user_input)
        return user_input
    except ValueError:
        pass


def get_user_input(player_guess_number):
    return player_guess_number

