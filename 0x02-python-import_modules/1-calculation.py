#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Call the imported functions with a and b as arguments, and print the results
print("a + b = ", add(a, b))
print("a - b = ", subtract(a, b))
print("a * b = ", multiply(a, b))
print("a / b = ", divide(a, b))
