import colorama
from colorama import Fore

"""
This file contains the messages to be displayed during the game.
"""


def welcome():
    print(Fore.LIGHTCYAN_EX + """


    $$$$               Welcome to Fortune Maker Game           $$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    $$$$$$$ 1 points = 1 million $$$$$$$
                     $$$$$$$ 2 points = 3 million $$$$$$$                                      
    ===========================================================================
              Guess correct 4 digit numbers and make fortunes!              
           Each level gets challenging, carefully use the help option. 
           In order to take the prize, you at least need to complete one level. 
    ===========================================================================  
                   """)


def good_bye():
    print(Fore.RED + "Thank you for playing!!!")
