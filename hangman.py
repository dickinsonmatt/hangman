import random
import json
import string
from getpass4 import getpass


sep = ""

def word_selection(file):
    with open(file) as inp:
        data = json.load(inp)


    words = data['data']

    target = data['data'][random.randint(0, (len(words)-1))]

    return target


def hiding(wrd):

    word_length = len(wrd)

    blank = "_"*word_length

    return blank

def char_frequency(string):
    char_dict = {}
    for i in range(len(string)):
        if string[i] in char_dict:
            char_dict[string[i]] += [i]

        else:
            char_dict[string[i]] = [i]

    return char_dict


def guess(selection, hidden, lives = 6, hard_mode = False):

    # print(f"{hard_mode} mode")
    correct = False

    guess_list = ""
    correct_list = ""
    wrong_list = ""

    # target_list = list(selection)
    hidden_list = list(hidden)

    word_counts = char_frequency(selection)
    # print(word_counts)
    if " " in selection:
        for i in word_counts[" "]:
            hidden_list[i] = " "

    while lives > 0:

        print(sep.join(hidden_list))

        g = input("Please enter a letter to guess: ").lower()
        
        while len(g) != 1 or len(g) == len(selection) or g not in string.ascii_letters or g in guess_list:
            
            if len(g) == len(selection):
                print("You have opted to guess the enter word")
                if g == selection:
                    correct = True
                    break
                else:
                    print("Unfortunately, you got it wrong")
                    lives -= 1
            else:
                print('Either:\n1. The letter you entered is not a valid letter \n2. You entered too many letters \n3. You have already guessed that letter')

                g = input("Please enter a letter to guess: ").lower()

        if hard_mode == True:
            while g in "aeiou":
                print("You have chosen hard mode. No vowels are allowed. Choose another letter.")

                g = input("Please enter a non-vowel letter: ").lower()

        guess_list += g           

        if correct == True:
            break

        elif g in selection:
            correct_list += g
            for i in word_counts[g]:
                hidden_list[i] = g            

        else:
            print("That letter is not present")
            wrong_list += g
            lives -= 1

        

        print(f"Lives remaining: {lives}")
        print()

        if "_" not in hidden_list:
            break

    if lives <= 0:
        print(f"You've run out of lives. The correct word was '{selection}'")
    
    else:
        print("Congratulations! You guessed the word correctly!")

    return lives


if __name__ == "__main__":
    play = True
    mode = False
    score = 0
    tries = 6

    while play:
        # make user choose a random word or put in a phrase themselves
        ask = input("Would you like to enter your own word? (y/n) ").lower()
        ask2 = input("Would you like to play on hard mode? (y/n) ").lower()

        while ask and ask2 not in ['y', 'n']:
            ask = input("Word choice: Please enter 'y' or 'n' ")
            ask2 = input("Hard mode: Please enter 'y' or 'n' ")

        if ask == "y":
            print("Please enter the word or phrase you would the user to guess")
            word = getpass("Phrase: ").lower()
        
        else:
            print("Choosing random word")
            word = word_selection('words.json')

        if ask2 == "y":
            tries = 3
            mode = True

        blanked = hiding(word)

        score += guess(word, blanked, lives = tries, hard_mode = mode)
        print(f"You scored {score} points in that round!")

        print()

        play = bool(input("Enter anything to play again! "))

        print("-----"*8)

    print()
    print(f"You scored {score} points total")
    print("Thanks for playing! Bye Bye!")


