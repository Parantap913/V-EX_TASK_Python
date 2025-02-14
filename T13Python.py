# Write a Python program to check if a given string contains only digits using regex.
import re

def check(ip):
    pattern = r'^\d+$'
    
    if re.match(pattern, ip):
        return True
    else:
        return False

ip = "123456"
if check(ip):
    print("The string", ip, "contains only digits.")
else:
    print("The string", ip, "does not contain only digits.")

# Explain the difference between re.search() and re.match().
# re.search(): searches the entire string for a match to the regular expression.
# re.match(): checks if the regular expression matches only at the beginning of the string.

# Write a program to extract all email addresses from a given text using regex.
import re

def check_email(text):
    e_pattern = r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(e_pattern, text)
    
    return emails

sample = """
    Hello, please contact us at abc@example.com for more details.
    admin@company.org
    Thank you!
"""

# Extract emails from the sample text
extracted_emails = check_email(sample)

print("Extracted email addresses:")
for e in extracted_emails:
    print(e)

# What is the purpose of re.sub() in Python?
# Used to search for a pattern in a string and replace it with another string.
import re

text = "I like apple and apple juice."
r = re.sub('apple', 'orange', text)

print(r)

# Write a regex pattern to validate a strong password.
# ^
