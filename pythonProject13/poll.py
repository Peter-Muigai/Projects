# Programming poll.

filename = 'programming_poll.txt'
print("Welcome to a programming poll.")
print("Enter 'quit' anytime to stop.")

while True:
    voter = input("Enter your name: ")
    if voter.lower() == 'quit':
        print("Thanks for participating!")
        break

    reason = input(f"{voter.title()} why do you love programming? ")
    if reason.lower() == 'quit':
        print("Thanks for participating!")
        break

    print("Awesome! Your response has been recorded.\n")

    # Writing the name and reasons for loving programming in append mode.
    with open(filename, 'a') as file_object:
        file_object.write(f"{voter.title()}\n")
        file_object.write(f"{reason}\n")