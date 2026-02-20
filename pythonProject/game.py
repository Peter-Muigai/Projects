alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("Player just earned 5 points")

# Next level
print("\n")
alien_color = 'yellow'
if alien_color == 'green':
    print("Earned 5 points!")
else:
    print("Earned 10 points!")

# Next level
print("\n")
alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
elif alien_color == 'red':
    point = 15
print(f"Player has earned {point}.")