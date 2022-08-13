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
        log_error().warning(e)

    finally:
        curser.close()
        conn.close()


def create_table_player():
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS player (player_id INT AUTO_INCREMENT PRIMARY KEY,"
            " username VARCHAR(255) NOT NULL UNIQUE,"
            " email VARCHAR(255)  NOT NULL UNIQUE,"
            "account_created TIMESTAMP NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS score_board (player_id INT, level INT, points INT, prize_amount "
                       "INT, date_time TIMESTAMP NOT NULL, FOREIGN KEY (player_id) REFERENCES player(player_id))")

        conn.commit()

    except Exception as message:
        # noinspection PyUnresolvedReferences
        log_error.warning(message)

    except Error as e:
        log_error().debug(e)

    finally:
        cursor.close()
        conn.close()


def insert_player(username, email):
    try:
        insert_query = "INSERT INTO player(username, email) VALUES(%s, %s)"
        args = (username, email)
        connect_db(insert_query, args)

    except OperationalError as e:
        log_error().warning(e)


def insert_score_board(player_id, level, points, prize_amount, date_time):
    try:
        insert_query = "INSERT INTO score_board(player_id, level, points, prize_amount, date_time) VALUES(%d, %d, %d, " \
                       "%d, " \
                       "%r) "
        args = (player_id, level, points, prize_amount, date_time)

        connect_db(insert_query, args)

    except OperationalError as e:
        log_error().warning(e)
