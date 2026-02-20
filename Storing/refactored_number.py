import json

def get_stored_number():
    """Get the stored favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_number():
    """Prompt for a new favorite number and store it."""
    filename = 'favorite_number.json'
    while True:
        try:
            number = int(input("What's your favorite number? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    with open(filename, 'w') as f:
        json.dump(number, f)
    return number


def remember_favorite_number():
    """Report the stored number or prompt for a new one."""
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = get_new_number()
        print(f"I'll remember that your favorite number is {number}!")


# Run the program
remember_favorite_number()
