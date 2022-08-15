# Name: Fortune_Maker_Game 
Programming Language: Python
Database Management Tool: MySQl server
IDE: Pycharm CE
UI for the game is CLI.

# Project Description
Created a Fortune Maker Game. This is game is played against computer. Computer 
generates four number combination between 0 and 7. Similarly, player gets to guess the 
number that computer generated following all the requirements to guess.

There is two level is this game.
1. Land (easier than sky)
2. Sky

Each level contains few attempts and player also gets hint option to guess.

# All the requirements for the program to successfully run are listed in requirements.txt file.

# Tools
- MySQL Connector to access the database. Created database name "FortuneMakerGame" with
- Table names player and score_board.
- Web Scrapping performed to get computer number.
- Flask to create an api endpoint to access the player data.
- Pytest to test some functions of the program.
- Git to track changes and GitHub to publish the project. 

# Created a new repository on GitHub "Fortune_Maker_Game"
- Cloned the repository on local your environment.
- Activated virtual environment (When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.)
    - python3 -m venv <package_name>
    - source package_name/bin/activate
- url to get the computer guess value: https://www.random.org/integers 


# To play the game
- Go to play_game.py under "models/play_game.py" python package.
- from the CLI, "python play_game.py"
- FYI: MySQL connection might be an issue. Help: "https://www.mysqltutorial.org/python-mysql/"
- 
# See the api endpoint in /models/api.py






