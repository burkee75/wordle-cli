from string import printable
from prettytable import PrettyTable
from random import randrange
from rich import print
import sys


def main():
    # first we must load only 5 letter words to save RAM
    word_list = []
    with open('/usr/share/dict/words', 'r') as words_file:
        for line in words_file:
            word = line.rstrip()
            if len(word) == 5:
                word_list.append(word.lower())

    #print(word_list)

    # pick a random word from the list. Need to ensure the randome number falls within the list indices range.
    word_list_range = randrange(len(word_list))

    # wordle_word is manually set for testing purposes right now. 
    wordle_word = "HELLO"
    wordle_word_list = []

    # don't think I need this anymore
    #for a in wordle_word:
    #    wordle_word_list.append(a)


    # wordle_word = word_list[word_list_range]
    # for debug
    print(f"Debug: Wordle word is: '{wordle_word}'")

    ## Each column is a list that will be added to during each guess.
    letter_1_list = []
    letter_2_list = []
    letter_3_list = []
    letter_4_list = []
    letter_5_list = []



    print("""\nWORDLE-CLI
    ----------
    Guess the WORDLE in 6 tries.
    Each guess must be a valid 5 letter word. Hit the enter button to submit.
    After each guess, the color of the letters will change to show how close your guess was to the word.
    """)

    wordle_table = PrettyTable()
    wordle_table.field_names = ["Letter 1", "Letter 2", "Letter 3", "Letter 4", "Letter 5"]


    # initialize some varibales
    guess_count = 0
    guess_word = ""
    guess_word_list = []


    while guess_count < 5:
        # TODO: need to reset objects (delete maybe?) after a bad guess. Right now color will stay white. 
        print(f"\nGuess #{guess_count +1}")
        guess_word = input("Guess a word: ")
        guess_word = guess_word.upper()
        # TODO: check if characters are letters.
        # TODO: convert input to lower case
        #while len(guess_word) < 5:
            #print("Your word was not 5 characters, try again.")
            # need to construct the table showing each letter in a column

        # add to our guess list of words
        guess_word_list.append(guess_word)
        # for debug
        #print(guess_word_list)

        for guess in guess_word_list:
            output = ""
            for i in range(len(guess)):
                if guess[i] == wordle_word[i]:
                    letter_color = f"[green]{guess[i]}[/green]"
                    output = output + letter_color
                elif guess[i] in wordle_word:
                    letter_color = f"[yellow]{guess[i]}[/yellow]"
                    output = output + letter_color

                else:
                    letter_color = guess[i]
                    output = output + letter_color

            print(output)


        #wordle_table.add_row([guess_word_list[0], guess_word_list[1], guess_word_list[2], guess_word_list[3], guess_word_list[4]])
        #print(wordle_table)
        if guess_word == wordle_word:
            print("\nYOU WIN!!!\n")
            sys.exit()

        guess_count += 1


if __name__ == '__main__':
    main()
