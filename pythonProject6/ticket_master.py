age = int(input("Enter your age to get the ticket price: "))
if age < 3:
    print("Your ticket is free!")
elif age <= 12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")