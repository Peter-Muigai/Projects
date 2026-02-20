# Lottery that depends on random ticket numbers and letters.
import random

# List containing 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items
winning_combo = random.sample(items, 4)

# Print result
print("Winning ticket:", winning_combo)
print("Any ticket matching these four items wins a prize!")
