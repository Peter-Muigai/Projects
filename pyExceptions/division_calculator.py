# A simple division Calculator.
print("Give me two numbers, and I will divide them. ")
print("Enter 'quit' anytime to stop.")

while True:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'quit':
        break
    second_number = input("\nSecond number: ")
    if second_number.lower() == 'quit':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)