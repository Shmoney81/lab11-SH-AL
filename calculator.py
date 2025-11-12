import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        print("Invalid input")
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    if a<=0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    return a ** b


