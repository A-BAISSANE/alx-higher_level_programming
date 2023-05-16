#!/usr/bin/python3
# 0-print_list_integer.py
def print_list_integer(my_list=[1, 2, 3, 4, 5]):
    for num in my_list:
        print("{:d}".format(num))

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
