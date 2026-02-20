# Step 1: Set up the game
secret_word = "python"
guessed_letters = []
display = ["_" for _ in secret_word]
lives = 6  # Max number of wrong guesses

print("Welcome to Hangman!")
print(" ".join(display))

# Step 3: Loop until game ends
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display[index] = guess
        print("Good job!")
    else:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")

    print(" ".join(display))
    print()

# Step 4: Game Over
if "_" not in display:
    print("🎉 You won! The word was:", secret_word)
else:
    print("😢 Game over! The word was:", secret_word)
