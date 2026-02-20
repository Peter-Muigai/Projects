import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print("I don't know your favorite number yet.")
except json.JSONDecodeError:
    print("The data seems corrupted, please enter it again.")
else:
    print(f"I know your favorite number! It's {number}.")