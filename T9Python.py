# Write a Python program to read a file and print its contents.
f1 = open("myfile.txt", "r")
print(f1.read())
f1.close()

# Explain the difference between r, w, a, and r+ modes in file handling.
# r: Opens the file for reading.
# w: Opens the file for writing.(overwrite existing contents)
# a: Opens the file for appending new content.
# r+: Opens the file for both reading and writing.

# Write a program to copy the contents of one file to another.
source = "source.txt"
destination = "destination.txt"

src = open("source.txt", "r")

# Read the contents of the source file
content = src.read()
src.close()

dest = open("destination.txt", "w")

# Write the content to the destination file
dest.write(content)
dest.close()

print(source, destination)

# Write a Python script to count the number of words in a file.
file = "count.txt"

file = open("count.txt", "r")
content2 = file.read()
    
# Split the content into words based on whitespace and count the number of words
words = content2.split()
word_count = len(words)

print("The number of words in the file is:", word_count)

# What is the use of the with statement in file handling?
# Automatically closes the file when the block of code inside the with statement is finished.

# with open("file.txt", "r") as file:
# content = file.read()
# print(content)
# No need to call file.close()




