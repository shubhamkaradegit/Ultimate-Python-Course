l = ["apple", "banana", "cherry"]

l[2] = 'y'
print(l)

a = "shubham"



# a[3] = 'z'
# print(a)  # this will give an error because strings are immutable

# Append an element to the end of the list
l.append("orange")
print("After append:", l)

# Insert an element at a specific position
l.insert(1, "blueberry")
print("After insert:", l)

# Remove an element from the list
l.remove("banana")
print("After remove:", l)

# Pop an element from the list
popped_element = l.pop()
print("After pop:", l)
print("Popped element:", popped_element)

# Find the index of an element
index = l.index("apple")
print("Index of 'apple':", index)

# Count the occurrences of an element
count = l.count("apple")
print("Count of 'apple':", count)

# Sort the list
l.sort()
print("After sort:", l)

# Reverse the list
l.reverse()
print("After reverse:", l)

# Clear the list
l.clear()
print("After clear:", l)

