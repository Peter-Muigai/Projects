def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
    else:
        return"Invalid operation!"

print(calculate(10, 5, "add"))
print(calculate(10, 0, "divide"))
print(calculate(4, 2, "modulus"))



