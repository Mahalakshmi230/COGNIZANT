from math import *

def math_operations(num):
    if num >= 0:
        print(f"Square Root: {sqrt(num):.2f}")
        print(f"Power: {pow(num, 2):.2f}")
        print(f"Value of Pi: {pi:.2f}")
    else:
        print("Invalid input")

num = 16

math_operations(num)