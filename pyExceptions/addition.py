# A simple addition of two integers.
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
try:
    answer = float(first_number) + float(second_number)
    print(answer)
except ValueError:
    print("Oops! That doesn't look like a number. Please enter digits only.")
