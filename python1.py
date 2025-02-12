# 1
# Write a Python program to print "Hello, World!".
print("Hello, World!")

# Write a program to take user input for their name and print a greeting message.
username1 = input("Enter your name: ")
print("Hello, " + username1 + " Welcome to Python Programming.")

# What is the difference between print() and input() in Python?
# print: display output to the user.
# input: take input from the user.

# Write a program to swap two variables without using a third variable.
a1 = 5
b1 = 10

a1, b1 = b1, a1

print("After swapping: a =", a1, ", b =", b1)

# Write a Python script to check the type of a variable.
x1 = 10
print(type(x1))

# 2
# What are mutable and immutable data types in Python?
# Mutable : values can be changed after creation.
# Immutable : values cannot be changed after creation.

# Write a program to convert an integer to a string and vice versa.
num2 = 1234
num_str2 = str(num2)
print(num_str2)

str2 = "123"
str_num2 = int(str2)
print(str_num2)

# Write a program to check if a number is of integer type.
def f2(n2):
    return isinstance(n2, int)
print(f2(5))
print(f2(5.5))

# What will be the output of print(type([]) is list)? Explain why.
print(type([]) is list)
# type([]) returns the type of an empty list: <class 'list'>.
# is checks whether type([]) is exactly the same object as list.

# Create a dictionary with three key-value pairs and print the value of a specific key.
dict2 = {
    'name': 'Parantap',
    'age': 21,
    'country': 'India'
}
print(dict2['age'])

# 3
# Write a Python program to demonstrate the use of all arithmetic operators.
a3 = 10
b3 = 5
print(a3 + b3)
print(a3 - b3)
print(a3 * b3)
print(a3 / b3)
print(a3 // b3)
print(a3 % b3)
print(a3 ** b3)

# What is the difference between is and == operators?
# is : checks whether two variables point to the same object in memory.
# == : checks whether the values of two variables are equal.
a = [1, 2, 3]
b = a
print(a is b)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# Write a Python program to check if a number is even or odd using conditional operators.

n3 = int(input("Enter the number to check even or odd:"))
if n3 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Explain the working of bitwise operators in Python with an example.
x3 = 10
y3 = 20
print(x3 & y3)
print(x3 | y3)
print(~x3)
print(x3 ^ y3)
print(x3 << y3)
print(x3 >> y3)

# Write a program to swap two numbers using bitwise XOR.
print("Enter two numbers for swap")
p3 = int(input("Enter first number p: "))
q3 = int(input("Enter second number q: "))

p3 = p3 ^ q3   
q3 = p3 ^ q3
p3 = p3 ^ q3

print("After swapping: p = ",p3, "q = ",q3)

# 4
# Write a program to check if a given number is positive, negative, or zero.
n4 = float(input("Enter the number to check positive,negative or zero:"))
if n4 > 0:
    print("Positive")
elif n4 < 0:
    print("Negative")
else:
    print("Zero")

# Write a Python program to print the first 10 numbers using a for loop.
for i4 in range(1, 11):
    print(i4)

# Write a Python program to calculate the factorial of a number using a while loop.
def f4(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

num4 = int(input("Enter the number to find factorial: "))
if num4 > 0:
    print("The factorial of" , num4 , "is ", f4(num4))

# What is the difference between break and continue statements? Give examples.
# break: Terminate the loop
# continue: skip the current iteration

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# Write a program to check whether a given year is a leap year.
year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(year, "is a leap year.")
elif (year % 100 == 0):
    print(year, "is not a leap year.")
elif (year % 4 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 5
# Write a function to find the sum of two numbers.
def sum(a,b):
    return a + b

print("Addition")
n5 = float(input("Enter the first number: "))
m5 = float(input("Enter the second number: "))

total = sum(n5, m5)
print("The sum of ", n5, "and ", m5, "is: ", total)

# Explain the difference between return and print() in functions.
# return: send a value back from a function.
# print: display information to the console.

# Write a recursive function to calculate the factorial of a number.
def fact(f): 
    if f == 0 or f == 1:
        return 1  
    else:
        return f * fact(f - 1)
    
print(fact(4))

# What is the use of *args and **kwargs in function definitions?
# *args: accept any number of arguments.
# **kwargs: accept any number of keyword arguments.

# Write a function that takes a list and returns a new list with only even numbers.
def f5(ip):    
    return [num5 for num5 in ip if num5 % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = f5(numbers)
print(even)

