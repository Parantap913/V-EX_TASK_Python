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