# Hangman/Guess The Word Game

Welcome to the Hangman Game! This is a Python console-based implementation of the classic word-guessing game where one player (the computer) randomly selects a word, and the other player (you) tries to guess it letter by letter. You have a limited number of incorrect guesses before you lose the game. The game provides visual feedback and keeps track of your progress.

## Game Features

- **Random Word Selection**: The game randomly selects a word from a predefined list.
- **Limited Guesses**: You have a total of 6 incorrect guesses before the game is over.
- **Progress Tracking**: The game displays the current state of the guessed word and the number of remaining attempts.
- **Visual Representation**: A simple ASCII art hangman is shown as you make incorrect guesses.
- **Input Validation**: The game handles invalid inputs, ensuring a smooth and user-friendly experience.
- **Replay Option**: After each game, you can choose to play again or exit.

## Requirements

- Python 3.10


## How to Play

1. **Clone the Repository**: Clone the project repository to your local machine using the following command:
   ```bash
   git clone https://github.com/Kumawat-Mukesh/hangman
   ```
2. **Navigate to the Project Directory: 
   ```bash
   cd hangman
   ```
3. **Run the Game: 
   ```bash
   Python Hangman.py
   ```

## Game Flow

- The computer selects a random word.
- You guess the word by entering one letter at a time.
- Each correct guess reveals the positions of the letter in the word.
- Each incorrect guess brings you one step closer to losing the game, represented visually by the hangman.
- You win if you correctly guess the entire word before running out of attempts.


## Example

```
Welcome to the HANGMAN!

------------------------------------------------------------------------
word : _ _ _ _ _ _
Guessed Letter : 
Remaining Attempts : 6

Guess a letter: P
Good Guess! The letter 'P' is in the word

------------------------------------------------------------------------
word : P _ _ _ _ _
Guessed Letter : P
Remaining Attempts : 6

Guess a letter: Z
Sorry, the letter 'Z' is not in the word

               -----
               |   |
               O   |
                   |
                   |
                   |
            --------
word : P _ _ _ _ _
Guessed Letter : P, Z
Remaining Attempts : 5

...

-----Result-----
Congratulations! You guessed the word 'PYTHON'.
-----      -----

```
