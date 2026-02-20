import random

# Lottery pool: 10 numbers + 5 letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 'A', 'B', 'C', 'D', 'E']

# Your chosen ticket (4 random unique items)
my_ticket = random.sample(lottery_items, 4)
print("Your ticket:", my_ticket)

attempts = 0

while True:
    attempts += 1
    # Generate a new random winning combination
    winning_ticket = random.sample(lottery_items, 4)

    # Check if your ticket matches
    if winning_ticket == my_ticket:
        print(f"\n🎉 You won after {attempts} draws!")
        print(f"Winning ticket: {winning_ticket}")
        break

    # Optional: show progress every 100,000 attempts (to avoid flooding output)
    if attempts % 100000 == 0:
        print(f"Still trying... {attempts} draws so far.")
