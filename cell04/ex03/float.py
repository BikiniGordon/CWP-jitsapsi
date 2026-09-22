#!/usr/bin/python3
try:
    n = float(input("Give me a nuber: "))
    if (n % 1 != 0):
        print("This number is a decimal.")

    else:
        print("This number is an integer.")

except ValueError:
    print("Error")