# A simple Addition Calculator.
print("Give me two numbers, and I will add them. ")
print("Enter 'quit' anytime to stop.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'quit':
        break
    second_number = input("\nSecond number: ")
    if second_number.lower() == 'quit':
        break
    try:
        answer = float(first_number) + float(second_number)
    except ValueError:
        print("Kindly input two integers.")
    else:
        print(f"The sum of {first_number} and {second_number} is {answer}.")
