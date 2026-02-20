print("=== Rock, Paper, Scissors Game ===")

# Get player names
player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

# Ask for choices
print("\nChoose from: rock, paper, scissors")

choice1 = input(f"{player1}, enter your choice: ").lower()
choice2 = input(f"{player2}, enter your choice: ").lower()

# Determine winner
if choice1 == choice2:
    print("It's a tie!")
elif (choice1 == "rock" and choice2 == "scissors") or \
     (choice1 == "scissors" and choice2 == "paper") or \
     (choice1 == "paper" and choice2 == "rock"):
    print(f"{player1} wins!")
elif (choice2 == "rock" and choice1 == "scissors") or \
     (choice2 == "scissors" and choice1 == "paper") or \
     (choice2 == "paper" and choice1 == "rock"):
    print(f"{player2} wins!")
else:
    print("Invalid input! Please enter rock, paper, or scissors.")
