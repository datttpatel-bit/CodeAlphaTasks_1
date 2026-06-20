# TASK 1: Hangman Game

import random

words = ["python", "hangman", "coding", "laptop", "banana"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman! ===")

while wrong_guesses < max_wrong:

    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord: ", display)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    if "_" not in display:
        print("🎉 You won! The word was:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        print("✅ Good guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        guessed_letters.append(guess)
        wrong_guesses += 1

if wrong_guesses == max_wrong:
    print("\n💀 Game Over! The word was:", secret_word)
