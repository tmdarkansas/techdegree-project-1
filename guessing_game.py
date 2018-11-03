"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("""
    *** Welcome to the fantastical number guessing game. ***
    
    Try your luck at guessing the correct number between 1 and 20.
    
    """)
    lowest_number = 0
    count = 0
    while True:
        if count == 0:
            random_number = random.randint(1,20)
            if lowest_number > 0:
                print("The best score (lowest number of guesses) is {}.  Try to beat that :) ".format(lowest_number))
        input_guess = input("Enter your guess: ")
        try:
            number_guess = int(input_guess)  
            if number_guess > 20 or number_guess < 1:
                raise ValueError("Please keep your guess between 1 and 20.  Please try again.")
        except ValueError as err:
            print("Please enter a valid integer value.")
            print("({})".format(err))
            print()
        else:
            count += 1
            if number_guess > random_number:
                print("It's lower")
            elif number_guess < random_number:
                print("It's higher")
            else:
                print("You guessed it!")
                print("It took you {} times to guess the correct answer.".format(count))
                if lowest_number > 0:
                    if lowest_number > count:
                        lowest_number = count
                        print("CONGRATULATIONS, you have the best score!")
                else:
                    lowest_number = count
                count = 0
                print()
                answer = input("Thanks for playing.  Enter 'Y' to play again: ")
                if answer.upper() == "Y":
                    print()
                    continue
                else:
                    break
    print()
    print("Come play again sometime, ya hear!")
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
