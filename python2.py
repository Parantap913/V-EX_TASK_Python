# 6
# Write a Python program to find the largest element in a list.
list1 = [10, 50, 30, 20, 70, 40]

largest = list1[0]

for n1 in list1:
    if n1 > largest:
        largest = n1

print("The largest element in the list is:", largest)

# What is the difference between a list and a tuple?
# list is mutable, modify it after creation(add, remove, or change elements).
# tuple is immutable, elements cannot be changed or modified.

# Write a Python program to reverse a list without using reverse().
mylist = [1, 2, 3, 4, 5]

reversed_list = mylist[::-1]

print("Reversed List:", reversed_list)

# Write a program to find the sum of all elements in a tuple.
tuple1 = (1, 3, 45, 29)
total = sum(tuple1)
print(total)

# Explain how list slicing works in Python with an example.
x1 = "Hello, World!"
print(x1[2:5])
print(x1[3:])
print(x1[:4])

# 7
# Write a Python program to check if a string is a palindrome.
def palindrome(s2):
    return s2 == s2[::-1]

ip1 = input("Enter a string to check palindrome or not: ")
if palindrome(ip1):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# What is the difference between split() and join() methods?
# split: used to break a string.
# join: used to combine a strings.

# Write a program to count the number of vowels in a given string.
ip2 = input("Enter a string to count vowels: ")

vowels = "aeiouAEIOU"
count = 0

for i2 in ip2:
    if i2 in vowels:
        count += 1

print(count)

# Write a Python program to replace all occurrences of a word in a string.
x2 = input("Enter a string:")
a2 = input("Enter the word to replace:")
b2 = input("Enter the replacement word:")

c2 = x2.replace(a2, b2)

print("Modified string:", c2)

# Explain how f-strings work in Python with an example.
name = "Parantap"
age = 21
height = 5.5

fs = f"Hello, my name is {name}, I am {age} years old, and my height is {height} feet."
print(fs)

# 8
# Write a Python program to merge two dictionaries.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}

dict3 = dict1 | dict2

print(dict3)

# How do you access a value from a dictionary safely without an error?
dict = {'a': 1, 'b': 2, 'c': 3}

v = dict.get('b')
print(v)

# Write a program to remove duplicates from a list using sets.
list1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

list2 = list(set(list1))

print(list2)

# Write a Python program to find the common elements between two sets.
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1 & set2
print(common)

# Explain how dictionary comprehensions work with an example.
# Dictionary comprehension to create a dictionary of squares
d = {x3: x3 + 2 for x3 in range(1, 6)}

print(d)






