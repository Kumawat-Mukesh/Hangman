import random

# Guess The Word/Hangman
# Create  a  Python  console-based  Guess  The  Word  (Hangman)  game  where  one player  thinks  of  a  word  and  the  other  player  tries  to  guess  it  letter  by  letter.  The  guessing  player  has  a  limited  number  of  incorrect  guesses  before they  lose. Display the progress of the guessed word, the remaining attempts, and a visual representation of the Hangman. Ensure the game handles invalid inputs and provides an engaging experience with a variety of word options.


class Hangman:
    def __init__(self, word):
        # self.word store the word
        self.word = word.upper()
        # Keep track of the letter that have been guessed by the user
        self.guessed_letter = []
        # Count the incorrect guesses
        self.incorrect_guesses = 0
        # User allowes only 6 incorect attempts
        self.attempts = 6
        # Unguessesd letter are shown as '_'
        self.display_word = ["_" for _ in self.word]

    def print_hangman(self):
        stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            --------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            --------
            """,
        ]

        print(stages[self.incorrect_guesses])

    def print_word(self):
        # Print the guessesd letter in their correct postions and unserscore ('_') for unguessed letter
        print("word : " + " ".join(self.display_word))

    def guess_word(self, letter):
        letter = letter.upper()
        # Check if the letter already guessed
        if letter in self.guessed_letter:
            print("You've already guessed the letter")
            return
        # If the letter not in the gueesed_letter, add to the list
        self.guessed_letter.append(letter)

        # If the letter in the word , update the letter to the correct position
        if letter in self.word:
            print(f"Good Guess! The letter '{letter}' is in the word")
            for i, char in enumerate(self.word):
                if char == letter:
                    # replace the letter to the correct position
                    self.display_word[i] = letter
        else:
            print(f"Sorry,  the letter '{letter}' is not in the word")
            self.incorrect_guesses += 1

    def is_word_guessed(self):
        # Check if the word guessed or not, return TRUE if he word guessed otherwise return FALSE
        return "_" not in self.display_word

    def game_over(self):
        # if the incorrect guesses are greater then the maximum attempts, then game is over
        return self.incorrect_guesses >= self.attempts

    def game_data(self):
        print(
            "------------------------------------------------------------------------"
        )
        self.print_hangman()
        self.print_word()
        print(f"Guessed Letter : {', '.join(self.guessed_letter)}")
        print(f"Remaining Attempts : {self.attempts - self.incorrect_guesses}")


def get_random_word():
    words = ["PYTHON", "HANGMAN", "PROGRAMMER", "CODE", "COMPUTER", "PROJECT"]
    return random.choice(words)


def main():
    print("Welcome to the HANGMAN!")
    game = Hangman(get_random_word())

    # The loop continue until the game over or the word is fully guessed
    while not game.game_over() and not game.is_word_guessed():
        game.game_data()
        guess = input("Guess a letter : ").upper()
        # Check input is valid or not (guessed letter == 1 and guessed letter isalpha)
        if len(guess) == 1 and guess.isalpha():
            # if the condition is true then pass the guess letter to the method
            game.guess_word(guess)
        else:
            print("Invalid Input. Please guess a single letter.")

    game.game_data()
    if game.is_word_guessed():
        print("-----Result-----")
        print(f"Congratulations! You guessed the word '{game.word}'.")
        print("-----      -----")

    else:
        print("-----Result-----")
        print(f"Game Over!\nSorry You loose the game!\n The word was '{game.word}'")
        print("-----      -----")

    if input("Do you want to play again? (y/n): ").lower() == "y":
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
