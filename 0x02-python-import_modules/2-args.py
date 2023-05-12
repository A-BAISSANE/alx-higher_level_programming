#!/usr/bin/python3
import sys

args = sys.argv[1:]
n_args = len(args)

print("Number of argument{}: {}".format("s" if n_args != 1 else "", n_args), end="")
print("{}\n".format(":" if n_args > 0 else "."))

for i in range(n_args):
    print("{}: {}\n".format(i + 1, args[i]))
