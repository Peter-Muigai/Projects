# A Simple polynomial calculator and login system.

# Default credentials
correct_username = "Admin"
correct_password = "Admin123"

# Maximum attempts allowed.
attempts = 3

# ___LOGIN PHASE___
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("welcome to  Polynomial Calculator!")
        break
    else:
        attempts -= 1
        print(f"Invalid username or password! You have {attempts} attempts remaining.")
        if attempts == 0:
            print("Too many failed attempts.Program terminated.")
            exit()

# ___POLYNOMIAL CALCULATOR___.
print("\n___Polynomial Calculator___")

records = []

for i in range(1, 6):
    print(f"Set{i}:")
    a = float(input("Enter a value for a: "))
    b = float(input("Enter a value for b: "))
    c = float(input("Enter a value for c: "))
    x = float(input("Enter a value for x: "))

    # Calculate polynomial.
    polynomial_value = a*(x**2) + b*x + c

    # Store the results
    records.append((a, b, c, x, polynomial_value))
    print()

# Display the results in a table.
print("\n==============Polynomial Results============\n")
print(f"{'a':>6} {'b':>8} {'c':>8} {'x':>8} {'Polynomial Value':>20}")
print("-" * 56)

for a, b, c, x, value in records:
    print(f"{a:6.1f} {b:8.1f} {c:8.1f} {x:8.1f} {value:20.2f}")

print("\n✅ All polynomial calculations completed successfully.")