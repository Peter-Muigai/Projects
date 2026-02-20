print("Lyrics generator")
print("Fill in the blanks")

correct_answer = "down"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    trial = input("Could you let me ____ slowly: ")
    attempts += 1

    if trial.lower() == correct_answer:
        print("That's right! 🎉")
        break
    else:
        print("Nope, try again!")

if attempts == max_attempts and trial.lower() != correct_answer:
    print("Out of tries! The correct answer was 'down'.")

print("You made", attempts, "attempt(s).")
print("Come back soon!")
