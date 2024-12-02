import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """,  # Final state: head, torso, both arms, and both legs
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,  # Head, torso, both arms, and one leg
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,  # Head, torso, and both arms
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,  # Head, torso, and one arm
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,  # Head and torso
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,  # Head only
        """
           -----
           |   |
               |
               |
               |
               |
        """,  # Initial empty state
    ]
    return stages[tries]

def get_word():
    word_list = ["python", "hangman", "Information", "internship", "Programming"]
    return random.choice(word_list).upper()

def play_hangman():
    word = get_word()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()  # Correctly guessed letters
    tries = 6
    guessed_word = ["_"] * len(word)

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word to guess: " + " ".join(guessed_word))

    while tries > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            print(f"Good job! {guess} is in the word.")
            guessed_letters.add(guess)
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            tries -= 1
            guessed_letters.add(guess)

        print(display_hangman(tries))
        print("Word to guess: " + " ".join(guessed_word))

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the game
play_hangman()
