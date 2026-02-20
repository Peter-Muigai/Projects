import random

while True:
    choice = input("Roll the Dice?(y/n): ")
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"{dice1}, {dice2}")
    elif choice == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
