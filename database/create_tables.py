from dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error


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

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


create_table_player()
