def welcome():
    print("""


    $$$$               Welcome to Fortune Maker Game           $$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    $$$$$$$ 3 points = 1 million $$$$$$$
                     $$$$$$$ 5 points = 5 million $$$$$$$                    
                   $$$$$$$ 10 points = 10 million $$$$$$$                   
                    $$$$$$$ 15 points = 15 million $$$$$$$                    
    ===========================================================================
              Guess correct 4 digit numbers and make fortunes!              
           Each level gets challenging, carefully use the help option. 
           In order to take the prize, you at least need to complete one level. :D    
    ===========================================================================  
                   """)


def winner():
    print("Hurray!!!! You won 15 million dollars.")
    print("Congratulations!!")


def good_bye():
    print("Thank you for playing!!!")



for i in range(4):
    player_guess_number = int(input(f"Enter Number {enumerate(i)}:"))
    print(player_guess_number)

