#!/usr/bin/python3
# Import the necessary functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Define variables a and b
a = 10
b = 5

# Call the imported functions with a and b as arguments, and print the results
print("a + b = ", add(a, b))
print("a - b = ", subtract(a, b))
print("a * b = ", multiply(a, b))
print("a / b = ", divide(a, b))
