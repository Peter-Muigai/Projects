"""This is a guests book entry."""
while True:
    guests = input("Welcome! Please enter your name: ")
    print(f"Good day {guests}.")
    break
filename = 'guests_book.txt'
with open(filename, 'w') as file_object:
    file_object.write(guests)
    
"""This is a guest book entry program."""

filename = 'guest_book.txt'

print("Welcome to the Guest Book!")
print("Enter 'quit' anytime to stop.\n")

while True:
    guest = input("Please enter your name: ")

    if guest.lower() == 'quit':
        print("Guest book has been updated. Goodbye!")
        break

    print(f"Good day, {guest}!")

    # Open the file in append mode so new guests are added instead of overwriting
    with open(filename, 'a') as file_object:
        file_object.write(f"{guest}\n")
