import random

def hangman():
    words = ["python", "codealpha", "developer", "program", "hangman"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("=== Welcome to Hangman Game! ===")
    print("Guess the word letter by letter.")

    while attempts > 0:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: ", display_word.strip())
        print(f"Remaining attempts: {attempts}")

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if attempts == 0:
        print(f"\n❌ Game Over! The correct word was: '{secret_word}'")

if __name__ == "__main__":
    hangman()
    