"""
Filename: Game_Center_V1.py
Author: Harri Baker
Date: 27/06/2022
Description: A program that acts like a game center. The user can pick and chose diffrent games to play.
"""

# Imports
import random

# Variables
menu_count = 0

# Lists
Game_names = ["Number Guesser",
              "Paper, Scissors, Rock, Lizard, Spock"
]
Yes_variants = ["YES", "YEs", "Yes", "yes", "yeS", "yES", "YE", "Ye", "ye", "yE", "Y", "y"]

# Dictionaries
Games = {
    "Number Guesser": "I choose a number between a certain range and you have to guess the number",
    "Paper": "It's like paper scissors rock but with more options",
}
# To help the menu look good
Space = {
    "Space_1": "        ",
    "Space_2": "                               "
}

# Functions
# Game 1
def Number_Guesser():
    
    # Variables
    number_guesser_range = 100
    user_number = -1
    keep_going = "yes"
    guessed_corect = False

    print("Welcome to Number Guesser")
    # Begin the Game
    while keep_going in Yes_variants:
        while user_number <= -1:

            # Variables
            computers_number = random.randrange(1,number_guesser_range)
            counter = 0

            user_number = int(input("Guess a number between 1 and {} \n".format(number_guesser_range)))
            while guessed_corect == False:
                try:
                    
                    if user_number > computers_number:
                        user_number = int(input("Your number is too high, guess again: "))
                        counter = counter + 1
                    
                    elif user_number < computers_number:
                        user_number = int(input("Your number is too low, guess again: "))
                        counter = counter + 1
                    
                    elif user_number == computers_number:
                        guessed_corect = True
                        counter = counter + 1
                    
                except ValueError:
                    print("Please enter a vaild number")
            
            
        # Reset Variables
        user_number = -1

        print("you gueessed correct. \nIt took you {} trys to get it right".format(counter))
        number_guesser_range += 100
        keep_going = input("would you like to go agian enter 'yes' if you want to  ")
# Game 2
def PSRLS():
    # List
    Options = ["Paper", "Scissors", "Rock", "Lizard", "Spock"]
    
    # Variables
    player_score = 0
    computer_score = 0
    tie = 0
    user_option = 0
    computer_option = random.randrange(1,6)
    
    print("Wellcome to {}".format(Game_names[1]))

    # Rules
    print("")
    print("Here are the rules:")
    print("{} beats {} and {}".format(Options[0],Options[2],Options[4]))
    print("{} beats {} and {}".format(Options[2],Options[1],Options[3]))
    print("{} beats {} and {}".format(Options[1],Options[3],Options[0]))
    print("{} beats {} and {}".format(Options[3],Options[4],Options[0]))
    print("{} beats {} and {}".format(Options[4],Options[2],Options[1]))
    
    # Let the game begin
    while user_option < 1 or user_option > 5:
        try:
            user_option = int(input("""What option do you want?
                                    1. Paper
                                    2. Scissors
                                    3. Rock
                                    4. Lizard
                                    5. Spock
                                    """))
        except ValueError:
            print("\nPlease enter a vaild number")
    # Outcome Dictionaries
    User_choice = {
        "1" : paper,
        "2" : scissors,
        "3" : rock,
        "4" : lizard,
        "5" : spock
        }
    paper = {
        "1" : Draw,
        "2" : Lose,
        "3" : Win,
        "4" : Lose,
        "5" : Win
        }
    scissors = {
        "1" : Win,
        "2" : Draw,
        "3" : Lose,
        "4" : Win,
        "5" : Lose
        }
    rock = {
        "1" : Lose,
        "2" : Win,
        "3" : Draw,
        "4" : Win,
        "5" : Lose
        }
    Lizard = {
        "1" : Win,
        "2" : Lose,
        "3" : Lose,
        "4" : Draw,
        "5" : Win
        }
    Spock = {
        "1" : Lose,
        "2" : Win,
        "3" : Win,
        "4" : Lose,
        "5" : Draw
        }
    

def Menu():
    # Variables
    play = "yes"
    game_choice = -1
    game_choice_0 = False
    
    # Menu welcoming the user
    print()
    print("Hello there user, welcome to the game center. \nHere you will be able to play a game of your choosing from a variety of games \n\nHere is the menu:")
    print()
    print("Name: {} \nDescription: {} {}Enter 1 to play".format(Game_names[0],Games["Number Guesser"],Space["Space_1"]))
    print("Name: {} \nDescription: {} {}Enter 2 to play".format(Game_names[1],Games["Paper"],Space["Space_2"]))
    print("Enter 0 to leave")

    while play in Yes_variants:
        # Ask user what game they want to play
        while game_choice <= -1 or game_choice > 2:
            try:
                game_choice = int(input("\nWhat game would you like to play now? "))
                if game_choice > 2:
                    print("please enter a number in the menu")
                    print()
            except ValueError:
                print("Please enter a vaild number")
                print()
        # If the user entered 0 the program will end
        if game_choice == 0:
            print("Thank you for coming, I hope you come agian soon")
            game_choice_0 = True
            play = "no"
        # If the user entered 1 the program will run Number_Guesser()
        elif game_choice == 1:
            Number_Guesser()
            game_choice = -1
        # If the user entered 2 the program will run PSRLS()
        elif game_choice == 2:
            PSRLS()
            game_choice = -1
        
        elif game_choice_0 == False:
            play = input("Do you want to play agian? ")

Menu()
