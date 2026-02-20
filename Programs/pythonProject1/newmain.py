# main.py
import math_tools
import os

while True:
    print("\n--- Smart Math Helper ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")
    print("8. View History")

    choice = input("Choose an option (1-8): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = math_tools.add(a, b)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"{a} + {b} = {result}\n")

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = math_tools.subtract(a, b)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"{a} - {b} = {result}\n")

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = math_tools.multiply(a, b)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"{a} * {b} = {result}\n")

    elif choice == '4':
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = math_tools.divide(a, b)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"{a} / {b} = {result}\n")

    elif choice == '5':
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        result = math_tools.power(a, b)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"{a} ^ {b} = {result}\n")

    elif choice == '6':
        x = float(input("Enter number: "))
        result = math_tools.square_root(x)
        print("Result:", result)
        with open("history.txt", "a") as file:
            file.write(f"sqrt({x}) = {result}\n")

    elif choice == '7':
        print("Goodbye, Peter! 😊")
        break

    elif choice == '8':
        print("\n--- Calculation History ---")
        if os.path.exists("history.txt"):
            with open("history.txt", "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("History is empty.")
                else:
                    print(content)
        else:
            print("No history found yet.")

    else:
        print("Invalid choice. Please choose a number from 1 to 8.")
