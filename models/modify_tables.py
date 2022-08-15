from datetime import datetime

from dbconfig import read_db_config
from log import log_error
from mysql.connector import MySQLConnection, Error, OperationalError

"""

"""


def connect_db(insert_query, args):
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        curser = conn.cursor()
        curser.execute(insert_query, args)

        conn.commit()

    except Exception as e:
        log_error().warning(e)
        conn.rollback()

    finally:
        curser.close()
        conn.close()


def create_tables():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS player (player_id INT AUTO_INCREMENT PRIMARY KEY,"
            " username VARCHAR(255) NOT NULL UNIQUE,"
            " email VARCHAR(255)  NOT NULL UNIQUE,"
            "account_created TIMESTAMP NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS score_board (game_id INT AUTO_INCREMENT PRIMARY KEY, player_id INT "
                       "NOT NULL, "
                       "level INT NOT NULL, "
                       "points INT NOT NULL, prize_amount "
                       "INT NOT NULL, date_time TIMESTAMP NOT NULL, FOREIGN KEY (player_id) REFERENCES player("
                       "player_id))")

        conn.commit()

    except Error as e:
        log_error().warning(e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def insert_player(username, email, account_created):
    try:
        insert_query = "INSERT INTO player(username, email, account_created) VALUES(%s, %s, %s)"
        args = (username, email, account_created)
        connect_db(insert_query, args)

    except OperationalError as e:
        log_error().warning(e)

    except Exception as e:
        log_error().log(e)


def insert_score_board(game_id, player_id, level, points, prize_amount, date_time):
    try:
        insert_query = "INSERT INTO score_board(level, points, prize_amount, date_time) VALUES((%s, %s,%s, %s))"
        args = (level, points, prize_amount, date_time)

        connect_db(insert_query, args)

    except OperationalError as e:
        log_error().warning(e)


def select_player():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM player")
        player_data_list = []
        for i in cursor:
            player_data_list.append(i)
        return player_data_list
        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

