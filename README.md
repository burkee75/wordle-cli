# 🐍 wordle-cli
CLI Knock-Off of the Wordle game (https://www.powerlanguage.co.uk/wordle/). 
They maintain all copyright (now owned by The New York Times). 

## Requirements
- Must be played on a Linux/MacOS computer as it requires the `/usr/share/dict/words` file.
- Python 3.9+ (might work on lower versions, haven't tested)


# Playing the Game

## How to Play
Guess the WORDLE (5 letter word) in 6 tries.

Each guess must be a valid 5 letter word. Hit the enter button to submit.

After each guess, the color of the letters will change to show how close your guess was to the word.
- Green: the letter and position match the WORDLE word.
- Yellow: the letter is in the WORDLE word but in a different position.
- White: the letter is not in the WORDLE word. 

## Installing & Launching the Game 🕹
1. Clone the repo
2. Install the python packages: 
```bash
cd /path/to/download/
pip3 install -r requirements.txt
```

3. Launch the game: `python wordle-cli.py`. 
