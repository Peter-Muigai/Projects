import json

def greet_user():
    """Greet user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename, 'w'):
            json.dumps(username)
            print(f"We'll remember you when you come back {username}!")
    else:
        print(f"Welcome back {username}!")

greet_user()