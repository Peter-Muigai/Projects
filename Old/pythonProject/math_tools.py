# math_tools.py
import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
def power(a, b):
    return math.pow(a, b)
def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(x)

