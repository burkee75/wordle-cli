from string import printable
from prettytable import PrettyTable
from random import randrange
from rich import print
import sys


# This class will be used to build objects for each letter. Need this to help determine color for output. 
class LetterObject:
    def __init__(self, letter):
        self.letter_color = "white"
        self.letter = letter

    def print_format(self):
        """This method returns the letter's print string by combining the letter with the color to create 
        a character combo that will print in color."""
        
        if self.letter_color == "white":
            printable_letter = f"[white]{self.letter}[/white]"
            return printable_letter

        elif self.letter_color == "yellow":
            printable_letter = f"[yellow]{self.letter}[/yellow]"
            return printable_letter

        elif self.letter_color == "green":
            printable_letter = f"[green]{self.letter}[/green]"
            return printable_letter
    


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
wordle_word = "hello"
wordle_word_list = []
for a in wordle_word:
    wordle_word_list.append(a)


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
    guess_word = input("\nGuess a word: ")
    # TODO: check if characters are letters.
    # TODO: convert input to lower case
    #while len(guess_word) < 5:
        #print("Your word was not 5 characters, try again.")
        # need to construct the table showing each letter in a column
    
    # Convert the guess_word from input into objects for each letter
    for letter in guess_word:
        letter_object = LetterObject(letter)
        guess_word_list.append(letter_object)

    for d in range(len(guess_word_list)):
        if guess_word_list[d].letter in wordle_word_list:
            guess_word_list[d].letter_color = "yellow"
            # debug
            print(f"Letter {d} is white")

    for b in range(len(wordle_word_list)):
        #print(guess_word_list[b].print_format())
        if guess_word_list[b].letter == wordle_word_list[b]:
            guess_word_list[b].letter_color = "green"
            print(f"Letter {b} is green")
    

        #guess_word_list[item] = guess_word_list[item].print_format()
        
    for c in guess_word_list:
        print(c.print_format())

    #wordle_table.add_row([guess_word_list[0], guess_word_list[1], guess_word_list[2], guess_word_list[3], guess_word_list[4]])
    #print(wordle_table)
    if guess_word == wordle_word:
        print("\nYOU WIN!!!\n")
        sys.exit()

    guess_word_list = []       
    guess_count += 1
