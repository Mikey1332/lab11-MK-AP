"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Invalid input for square root")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b): # use math library + raise ValueError
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    a**b