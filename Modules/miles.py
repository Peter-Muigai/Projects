# A miles per gallon calculator.

# Default credentials.
username = "Admin"
password = "Admin123"

# Maximum attempts allowed.
attempts = 3

# __Login Phase__

while attempts > 0:
    user = input("Enter username: ")
    login = input("Enter password: ")
    if user == username and login == password:
        print("Welcome to Milage per gallon calculator!")
        break
    else:
        attempts -= 1
        print(f"Invalid username or password! You have {attempts} attempts remaining.")
        if attempts == 0:
            print("Too many failed attempts.Account locked.")
            exit()

# ___MPG Calculation phase___
print("\n ___Miles Per Gallon(MPG) Calculator___\n")

mpg_list = []
for i in range(1, 5):
    print(f"Trip{i}:")
    miles = float(input("Enter the miles driven: "))
    gallons = float(input("Enter the gallons of gas used: "))

    if gallons == 0:
        print("Gallons cannot be zero! Skipping this trip.")
        continue

    mpg = miles / gallons
    mpg_list.append(mpg)
    print(f"Miles per gallon(MPG) for trip{i}: {mpg:.2f}\n")

# ___Final Results___
if mpg_list:
    average_mpg = sum(mpg_list) / len(mpg_list)
    print("___Summary___")
    for i, value in enumerate(mpg_list, 1):
        print(f"Trip {i}: {value:.2f} MPG")
        print(f"\nAverage MPG across {len(mpg_list)} trips: {average_mpg:.2f}")
else:
    print("No valid MPG data to calculate average.")
