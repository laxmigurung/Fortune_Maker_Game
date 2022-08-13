from dbconfig import read_db_config
from log import log_error
from mysql.connector import MySQLConnection, Error


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as e:
        log_error(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


if __name__ == '__main__':
    connect()