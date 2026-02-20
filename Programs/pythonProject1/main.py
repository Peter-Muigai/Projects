import math_tools
while True:
        print("____Smart Math Helper_____")
        print(""""What operation do you want to perform?:
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    5.Power
    6.Square root
    7.Exit
    """)

     operation = input("Choose Operation(1-7): ")
     a = float(input("Enter first number: "))
     b = float(input("Enter second number: "))

    if operation == '1':
        result = math_tools.add(a, b)
    elif operation == '2':
        result = math_tools.subtract(a, b)
    elif operation == '3':
        result = math_tools.multiply(a, b)
    elif operation == '4':
        result = math_tools.divide(a, b)
    elif operation == '5':
        result = math_tools.power(a, b)
    elif operation == '6':
        result = math_tools.square_root()
    elif operation == '7':
        print("Exit")
    else:
        result = "Invalid operation"
    print("Result:", result)