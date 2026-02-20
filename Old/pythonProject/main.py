import calculator  # Import your custom module

print("Simple Calculator")
print("Choose operation: +, -, *, /")

operation = input("Operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == '+':
    result = calculator.add(a, b)
elif operation == '-':
    result = calculator.subtract(a, b)
elif operation == '*':
    result = calculator.multiply(a, b)
elif operation == '/':
    result = calculator.divide(a, b)
else:
    result = "Invalid operation"

print("Result:", result)
