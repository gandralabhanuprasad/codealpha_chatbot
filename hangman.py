import random

# List of words
words = ["python", "apple", "house", "chair", "ocean"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

incorrect_guesses = 0
max_incorrect = 6
guessed_letters = []

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
