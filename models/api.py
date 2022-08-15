import flask
from mysql.connector import MySQLConnection

from dbconfig import read_db_config
from modify_tables import select_player

app = flask.Flask(__name__)


# Created an api endpoint for player data.
@app.route('/', methods=['GET'])
def home():
    return "<h1>Fortune Maker Game</h1><p>Displaying player data in this api call. </p>"


@app.route('/player-data', methods=['GET'])
def display_player_data():
    return select_player()


app.run()
