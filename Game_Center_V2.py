"""
Filename: Game_Center_V2.py
Author: Harri Baker
Date: 27/06/2022
Description: A program that acts like a game center. The user can pick and choose different games to play.
"""

# Imports
import random

# Variables
menu_count = 0

# Lists
Game_names = ["Number Guesser",
              "Paper, Scissors, Rock, Lizard, Spock",
              "Tic Tac Toe",
]
Yes_variants = ["YES", "YE", "Y"]

# Dictionaries
Games = {
    "Number Guesser": "I choose a number between a certain range and you have to guess the number",
    "Paper": "It's like paper scissors rock but with more options",
    "Tic Tac Toe": "Try to get a 3 in a row on a 3 by 3 grid"
}
# To help the menu look good
Space = {
    "Space_1": "        ",
    "Space_2": "                               ",
    "Space_3": "                                          "
}

# Functions
# Game 1 Number Guesser
def Number_Guesser():
   
    # Variables
    number_guesser_range = 100
    user_number = -1
    keep_going = "yes"
    guessed_corect = False
    valid_user_number = False

    print("Welcome to Number Guesser")
    # Begin the Game
    while keep_going.upper() in Yes_variants:
        while user_number <= -1:

            # Variables
            computers_number = random.randrange(1,number_guesser_range)
            counter = 0

            # Ask the user to enter a number
            while not valid_user_number:
                try: # make sure the number is valid
                    user_number = int(input("Guess a number between 1 and {} \n".format(number_guesser_range)))
                    valid_user_number = True
                except ValueError:
                    print("Please enter a valid number")
                finally:
                    if valid_user_number:
                        if user_number < 1 or user_number > number_guesser_range:
                            print("\nThat number is invalid. Please enter a number from 1-{}".format(number_guesser_range))
                            valid_user_number = False

            while not guessed_corect:
                try: # Is the users number too high, too low, or just right
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
                    print("Please enter a valid number")
           
           
        # Reset Variables
        user_number = -1

        # Would the user like to go again and if they do the game will be harder
        print("you guessed correct. \nIt took you {} tries to get it right".format(counter))
        number_guesser_range += 100
        keep_going = input("would you like to go again enter 'yes' if you want to  ")

# Game 2 Paper Scissors Rock Lizard Spock
def PSRLS():
    # List
    Options = ["Paper", "Scissors", "Rock", "Lizard", "Spock"]
   
    # Variables
    player_score = 0
    computer_score = 0
    tie_score = 0
    user_option = 0
    computer_option = random.randrange(1,6)
    PSRLS_Keep_going = "yes"
   
    # Welcome
    print("Wellcome to {}".format(Game_names[1]))

    # Rules
    print("")
    print("Here are the rules\n")
    print("{} beats {} and {}".format(Options[0],Options[2],Options[4]))
    print("{} beats {} and {}".format(Options[2],Options[1],Options[3]))
    print("{} beats {} and {}".format(Options[1],Options[3],Options[0]))
    print("{} beats {} and {}".format(Options[3],Options[4],Options[0]))
    print("{} beats {} and {}".format(Options[4],Options[2],Options[1]))

    # Win, Lose, or Draw Dictionaries
    Paper = {"1":"Draw",
             "2":"Lose",
             "3":"Win",
             "4":"Lose",
             "5":"Win"
             }
    Scissors = {"1":"Win",
             "2":"Draw",
             "3":"Lose",
             "4":"Win",
             "5":"Lose"
             }
    Rock = {"1":"Lose",
             "2":"Win",
             "3":"Draw",
             "4":"Win",
             "5":"Lose"
             }
    Lizard = {"1":"Win",
             "2":"Lose",
             "3":"Lose",
             "4":"Draw",
             "5":"Win"
             }
    Spock = {"1":"Lose",
             "2":"Win",
             "3":"Win",
             "4":"Lose",
             "5":"Draw"
             }
    WLD = {
        "1":Paper,
        "2":Scissors,
        "3":Rock,
        "4":Lizard,
        "5":Spock
        }
    Word_PSRLS = {
        "1":"Paper",
        "2":"Scissors",
        "3":"Rock",
        "4":"Lizard",
        "5":"Spock"
        }

    # Loop
    while PSRLS_Keep_going.upper() in Yes_variants:
        # Let the game begin
        valid_input = False
        while not valid_input:
            try: # Get the users choice
                user_option = int(input("{} = 1 \n{} = 2 \n{} = 3 \n{} = 4 \n{} = 5 \nWhat option do you want? ".format(Options[0],Options[1],Options[2],Options[3],Options[4])))
                valid_input = True
            except ValueError:
                print("\nPlease enter a valid number between 1-5")
            finally:
                if valid_input:
                    if user_option > 5 or user_option < 1:
                        print("\nThat number is invalid. Please enter a number from 1-5. ")
                        valid_input = False

        # what the user entered, what the computer chose, and did the user win your lose
        print("You picked {} and the computer picked {}, you {}." .format(Word_PSRLS[str(user_option)], Word_PSRLS[str(computer_option)], WLD[str(user_option)][str(computer_option)]))

        # Scoring
        if WLD[str(user_option)][str(computer_option)] == "Win":
            player_score += 1
        elif WLD[str(user_option)][str(computer_option)] == "Lose":
            computer_score += 1
        elif WLD[str(user_option)][str(computer_option)] == "Draw":
            tie_score += 1

        PSRLS_Keep_going = input("Would you like to go again? ")
    print("You have a total score of {}, the computer got a score of {}, and you tied {} time/s" .format(player_score, computer_score, tie_score))

# Game 3 Tic Tac Toe
def Tic_Tac_Toe():

    # Imports
    import random
   
    # Variables
    user_choice_row = 0
    user_choice_column = 0
    computer_mark_attempt = 0
    win = 0
    lose = 0
    tie = 0
    play_again = "YES"
    complete = False
    computer_mark_done = False
    user_mark_done = False
    tie_option = False
   
    # Lists
    column = ["0", "1", "2", "3"]
    row_1 = ["1: ", "[]", "[]", "[]"]
    row_2 = ["2: ", "[]", "[]", "[]"]
    row_3 = ["3: ", "[]", "[]", "[]"]
   
    # Dictionaries
    ROWS = {"1": row_1,
            "2": row_2,
            "3": row_3}

    # Introduction
    print("Wellcome to Tic Tac Toe. \nHere you will play a game of Tic Tac Toe against the computer. \nThe rows are the numbers on the side of the grid and the columns are the number on the top of the grid.")
    print("Anyway that's enough for the introduction, Hace fun \n\n\n")
    
    # Begin
    print(column)
    print(row_1)
    print(row_2)
    print(row_3)

   
    while not complete:
        while not user_mark_done:
            while user_choice_row <= 0 or user_choice_row > 3:
                try:
                    user_choice_row = int(input("What row do you want to place your mark? "))

                except ValueError:
                    print("\nPlease enter a vaild number")
            while user_choice_column <= 0 or user_choice_column > 3:
                try:
                    user_choice_column = int(input("What column do you want to place your mark? "))

                except ValueError:
                    print("\nPlease enter a vaild number")
           
            if (ROWS[str(user_choice_row)])[user_choice_column] == "[]":
                user_mark_done = True
           
            elif (ROWS[str(user_choice_row)])[user_choice_column] != "[]":
                user_choice_row = 0
                user_choice_column = 0
                print("\nPlease place your mark in a empty space")
                
        print()
        
        # Set player mark
        if user_choice_row == 1:
            row_1[user_choice_column] = "X"
           
        elif user_choice_row == 2:
            row_2[user_choice_column] = "X"
           
        elif user_choice_row == 3:
            row_3[user_choice_column] = "X"

        # Win
        if row_1[1] == "X" and row_1[2] == "X" and row_1[3] == "X" or row_2[1] == "X" and row_2[2] == "X" and row_2[3] == "X" or row_3[1] == "X" and row_3[2] == "X" and row_3[3] == "X" or row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X" or row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X" or row_1[3] == "X" and row_2[3] == "X" and row_3[3] == "X" or row_1[1] == "X" and row_2[2] == "X" and row_3[3] == "X" or row_1[3] == "X" and row_2[2] == "X" and row_3[1] == "X":
            print("\nYou Win")
            complete = True
            tie_option = True
            computer_mark_done = True
            win = win + 1

        # Set computer mark
        while not computer_mark_done:
            computer_row = random.choice(list(ROWS.values()))
            computer_column = random.randrange(1,4)
            while computer_row[computer_column] == "X" or computer_row[computer_column] == "O":
                computer_row = random.choice(list(ROWS.values()))
                computer_column = random.randrange(1,4)
                computer_mark_attempt = computer_mark_attempt + 1
                if computer_mark_attempt >= 10:
                    break
            computer_row[computer_column] = "O"
            computer_mark_done = True

        print(column)
        print(row_1)
        print(row_2)
        print(row_3)

        # Lose
        if row_1[1] == "O" and row_1[2] == "O" and row_1[3] == "O" or row_2[1] == "O" and row_2[2] == "O" and row_2[3] == "O" or row_3[1] == "O" and row_3[2] == "O" and row_3[3] == "O" or row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O" or row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O" or row_1[3] == "O" and row_2[3] == "O" and row_3[3] == "O" or row_1[1] == "O" and row_2[2] == "O" and row_3[3] == "O" or row_1[3] == "O" and row_2[2] == "O" and row_3[1] == "O":
            print("\nYou lose")
            complete = True
            tie_option = True
            lose = lose + 1

        # Tie
        if computer_mark_attempt >= 10:
            if not tie_option:
                print("\nYou tied")
                complete = True
                tie = tie + 1

        # Play_again
        if complete == True:            
            play_again = input("Would you like to play again? \nEnter 'yes' if so: ")

            # Reset Variables
            column = ["0", "1", "2", "3"]
            row_1 = ["1: ", "[]", "[]", "[]"]
            row_2 = ["2: ", "[]", "[]", "[]"]
            row_3 = ["3: ", "[]", "[]", "[]"]

            ROWS = {"1": row_1,
                    "2": row_2,
                    "3": row_3}
            
            if play_again.upper() in Yes_variants:
                print("\n\n\n")
                print(column)
                print(row_1)
                print(row_2)
                print(row_3)
                
                complete = False

        # Reset Variables
        user_choice_row = 0
        user_choice_column = 0
        computer_mark_attempt = 0
        tie_option = False
        computer_mark_done = False
        user_mark_done = False
        game_over = False

    print("Thanks for playing Tic Tac Toe")
    print("You won {} time/s, You lose {} time/s, You tied {} time/s".format(win,lose,tie))
    print("Come again soon")

# Menu
def Menu():
    # Variables
    play = "yes"
    game_choice = -1
   
    # Menu welcoming the user
    print()
    print("Hello there user, welcome to the game center. \nHere you will be able to play a game of your choosing from a variety of games \n\nHere is the menu:")
    print()
    print("Name: {} \nDescription: {} {}Enter 1 to play".format(Game_names[0],Games["Number Guesser"],Space["Space_1"]))
    print("Name: {} \nDescription: {} {}Enter 2 to play".format(Game_names[1],Games["Paper"],Space["Space_2"]))
    print("Name: {} \nDescription: {} {}Enter 3 to play".format(Game_names[2],Games["Tic Tac Toe"],Space["Space_3"]))

    while play.upper() in Yes_variants:
        # Ask user what game they want to play
        while game_choice <= -1 or game_choice > 3:
            try:
                game_choice = int(input("\nWhat game would you like to play now? \nEnter 0 to leave "))
                if game_choice > 3:
                    print("Please enter a number in the menu")
                    print()
            except ValueError:
                print("Please enter a valid number")
                print()
        # If the user entered 0 the program will end
        if game_choice == 0:
            print("Thank you for coming, I hope you come again soon")
            play = "no"
        # If the user entered 1 the program will run Number_Guesser()
        elif game_choice == 1:
            game_choice = -1
            Number_Guesser()
        # If the user entered 2 the program will run PSRLS()
        elif game_choice == 2:
            game_choice = -1
            PSRLS()
        elif game_choice == 3:
            game_choice = -1
            Tic_Tac_Toe()

Menu()
