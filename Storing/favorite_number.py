import json

filename = 'favorite_number.json'
try:
    number = int(input("What's your favorite number? "))
except ValueError:
    print("Please enter a valid number.")
else:
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Got it, I'll remember it.")