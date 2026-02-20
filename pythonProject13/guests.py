"""This is a file of guests."""
guests = input("Welcome! Please enter your name: ")

filename = 'guests.txt'
with open(filename, 'w') as file_object:
    file_object.write(guests)