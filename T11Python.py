# Write a program to demonstrate try, except, finally blocks.
def f1():
    try:
        num1 = 10
        num2 = 0
        result = num1 / num2
        print("The result is:", result)
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    
    finally:
        # This block is always executed, regardless of success or failure
        print("This block is always executed, no matter what.")
f1()

# What is the difference between raise and assert statements?
# raise: Used to explicitly raise an exception in your code. Can raise any exception (custom or built-in).
# assert: Used to test conditions, typically for debugging. Tests a condition (raises AssertionError if False).

# Write a Python program to handle a ZeroDivisionError.
def divide(a, b):
    try:
        result = a / b
        print("The result of", a ,"divided by", b ,"is" , result)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
        
divide(10, 2)
divide(10, 0)

# What is the purpose of custom exceptions in Python?
# Custom exceptions give the ability to define & raise exceptions that are more meaningful for specific application.
# Helpful in diagnosing problems and improving debugging workflows.

# Write a function that raises a ValueError if the input is not a positive integer.
def f2(value):
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Input must be a positive integer.")
    return value

try:
    input = int(input("Enter a positive integer: "))
    f2(input)
    print("Valid input:", input)
except ValueError as e:
    print(e)


