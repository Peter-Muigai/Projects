import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("🤖 I'm thinking of a number between 1 and 100.")

while guess != number:
    guess = int(input("Your guess? "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempt(s).")
