# Attempt at wordle oh god what am I doing

# import
import random

"""
Filename:Wordle
Author:Liam Joyce
Date:started 27/6/22
Description: Wordle but in python (based off wordle but that's kinda obvious)
"""

# CONVERT .TXT TO STRING
# https://www.tutorialkart.com/python/python-read-file-as-string/
text_file = open("word_list_5.txt")

text = text_file.read()

text_file.close()

POTENTIAL_5_WORDS = text.split()

text_file = open("word_list_6.txt")

text = text_file.read()

text_file.close()

POTENTIAL_6_WORDS = text.split()

text = None


print("Welcome to Wordle in python!\n")
print("This game was made in PyScripter (there may be some indentation problems if you run it through idle)\n")
print("Y/yellow means correct letter, G/green means correct letter and position, N just means no, have fun ;)\n")

# Modules
def six_or_five():
    """Description: Determines if the user wants to play with 5 or 6 letter words"""
    five_or_six = "0"
    while five_or_six != "6" and five_or_six != "5":
        five_or_six = str(input("Would you like to play with 5 letter words or 6 letter words?\n")).strip().lower()
        if five_or_six == "6" or five_or_six == "six":
            print("6 Letter word it is!\n")
            five_or_six = "6"
            return five_or_six
        elif five_or_six == "5" or five_or_six == "five":
            print("5 letter word it is!\n")
            five_or_six = "5"
            return five_or_six
            pass
        else:
            print("That is NOT a valid input\n")
    return five_or_six



def player_guess(five_or_six):
    """Gets the player's guess and returns it (5 letter)"""
    if five_or_six == "5":
        guess = str(input("Please enter a 5 letter word:\n")).strip().upper()  # Prompts user to enter a word
        while len(guess) != 5 or not guess.isalpha():  # Making sure that a valid word has been entered.
            if not guess.isalpha():  # Tells the user what they did wrong
                guess = str(input("Please enter an actual 5 LETTER word:\n")).strip().upper()
            else:  # Tells the user what they did wrong
                guess = str(input("Please enter a  F I V E  letter word:\n")).strip().upper()
        print("You guessed the word \"{}\"".format(guess))
        return guess
    elif five_or_six == "6":
        guess = str(input("Please enter a 6 letter word:\n")).strip().upper()  # Prompts user to enter a word
        while len(guess) != 6 or not guess.isalpha():  # Making sure that a valid word has been entered.
            if not guess.isalpha():  # Tells the user what they did wrong
                guess = str(input("Please enter an actual 6 LETTER word:\n")).strip().upper()
            else:  # Tells the user what they did wrong
                guess = str(input("Please enter a S I X letter word:\n")).strip().upper()
        print("You guessed the word \"{}\"".format(guess))
        return guess


def compare(guess, attempt, word):
    """Description: Marks where correct letters are and compares the player guess to the randomly chosen word"""
    # Word check (correct)
    if guess == word:
        if attempt == 1:
            print("Congratulations! It took you... {} attempt... how?".format(attempt))
            attempt = 6
            win = True
            return True
        else:
            print("Congratulations you did it! It took you {} attempts!".format(attempt))
            attempt = 6
            win = True
            return True
    status = []

    # Word check (compare)
    # Also for a bit of context, word.find() returns -1 if nothing was found

# Reset variables~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    position = -1
    position_c = -1
    instances = []
    correct = []
    status = []
# Get letter instances~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for letter in word:
        instances.append(letter)
# Mark correct positions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for index in range(len(guess)):
        position_c += 1
        if word[index].find(guess[index]) != -1:
            correct.append(position_c)
            try:
                instances.remove(guess[index])
            except:
                pass
# Start of for loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for i in range(len(guess)):
        position += 1
    # Correct~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if word[i].find(guess[i]) != -1:
            status.append("G")
    # Correct letter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        elif word.find(guess[i]) != -1:
            if guess[i] in instances and position not in correct:
                status.append("Y")
                try:
                    instances.remove(guess[i])
                except:
                    pass
# Correct letter but no new instances~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            else:
                status.append("N")

    # Wrong ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            status.append("N")
    # Spacing
    print(status)

def main():
    """Description: Main game"""
    # MAIN GAME
    # Variables
    attempt = 0
    win = False
    replay = "yes"
    # Repeats while the user still wants to play
    while replay == "yes" or replay == "y":
        # Sets the length of the selected word
        five_or_six = six_or_five()
        if five_or_six == "5":
            word = random.choice(POTENTIAL_5_WORDS).upper().strip()
        elif five_or_six == "6":
            word = random.choice(POTENTIAL_6_WORDS).upper().strip()
        # Repeats while the user is still guessing
        while attempt != 6 and not win:  # Makes sure you don't going over the attempt limit
            attempt += 1  # Counts attempts
            print("You are currently on attempt {}/6\n".format(attempt))
            guess = player_guess(five_or_six)
            win = compare(guess, attempt, word)
        if not win:
            print("You lost! The word was {}".format(word))
        replay = str(input("Would you like to play again? (y, n)")).lower().strip()
        while replay != "y" and replay != "yes" and replay != "n" and replay != "no":
            replay = str(input("Would you like to play again? (y, n)")).lower().strip()
        attempt = 0
        win = False
    print("Goodbye!")
    # GAME END

main()
