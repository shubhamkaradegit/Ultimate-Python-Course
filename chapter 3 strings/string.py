name = "shubham"   
#string are immutable

print(name[1:6:2])

#output: hba

# Most used string functions in Python

# Convert to uppercase
print(name.upper())

# Convert to lowercase
print(name.lower())

# Capitalize the first letter
print(name.capitalize())

# Find the position of a substring
print(name.find('ub'))

# Replace a substring with another substring
print(name.replace('shubham', 'Shubham'))

# Check if the string starts with a specific substring
print(name.startswith('shu'))

# Check if the string ends with a specific substring
print(name.endswith('ham'))

# Split the string into a list
print(name.split('b'))

# Join a list of strings into a single string
print('-'.join(['shubham', 'is', 'learning', 'python']))

# Remove whitespace from the beginning and end of the string
print(name.strip())
# Output:
# hba
# SHUBHAM
# shubham
# Shubham
# 2
# Shubham
# True
# True
# ['shu', 'ham']
# shubham-is-learning-python
# shubham
