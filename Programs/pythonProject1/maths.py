import math_tools  # Your custom functions

while True:
    print("\n--- Smart Math Helper ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", math_tools.add(a, b))

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", math_tools.subtract(a, b))

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", math_tools.multiply(a, b))

    elif choice == '4':
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result:", math_tools.divide(a, b))

    elif choice == '5':
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result:", math_tools.power(a, b))

    elif choice == '6':
        x = float(input("Enter number: "))
        print("Result:", math_tools.square_root(x))

    elif choice == '7':
        print("Goodbye, Peter! 😊")
        break  # 🔑 This ends the loop and exits the program

    else:
        print("Invalid choice. Please choose a number from 1 to 7.")
