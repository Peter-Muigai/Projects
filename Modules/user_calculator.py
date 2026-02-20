# A User based Calculator
import calculator

while True:
    print("\nA Simple Calculator.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.Exit")

    choice = input("Choose an option(1-5). ")
    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        if choice == '1':
            print("Results= ", calculator.add(a, b))
        elif choice == '2':
            print("Results= ", calculator.subtract(a, b))
        elif choice == '3':
            print("Results= ", calculator.multiply(a, b))
        elif choice == '4':
            print("Results= ", calculator.divide(a, b))
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid option try again.")
