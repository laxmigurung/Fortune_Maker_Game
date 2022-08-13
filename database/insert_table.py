from dbconfig import read_db_config
from log import log_error
from mysql.connector import MySQLConnection, Error, OperationalError


def connect_db(insert_query, args):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        curser = conn.cursor()
        curser.execute(insert_query, args)

        conn.commit()
    except Error as e:
        log_error(e)

    finally:
        curser.close()
        conn.close()


def insert_player(username, email):
    try:
        insert_query = "INSERT INTO player(username, email) VALUES(%s, %s)"
        args = (username, email)
        connect_db(insert_query, args)

    except OperationalError as e:
        log_error(e)


def insert_score_board(player_id, level, points, prize_amount, date_time):
    try:
        insert_query = "INSERT INTO score_board(player_id, level, points, prize_amount, date_time) VALUES(%d, %d, %d, " \
                       "%d, " \
                       "%r) "
        args = (player_id, level, points, prize_amount, date_time)

        connect_db(insert_query, args)

    except OperationalError as e:
        log_error(e)


def get_user_input(player_guess_number):
    return player_guess_number
