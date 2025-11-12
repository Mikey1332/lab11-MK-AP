"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b): # use math library + raise ValueError
    return math.log(b, a)

def exp(a, b):
    a**b