tuple = (1, 2, 3, 4, 5)
"""
This script demonstrates various operations on a tuple in Python.
Tuple:
Operations:
    1. Accessing elements:
        - Access the first element: tuple[0]
        - Output: 1
    2. Slicing:
        - Slice elements from index 1 to 2: tuple[1:3]
        - Output: (2, 3)
    3. Length of tuple:
        - Get the number of elements in the tuple: len(tuple)
        - Output: 5
    4. Count occurrences of an element:
        - Count how many times the element 3 appears in the tuple: tuple.count(3)
        - Output: 1
    5. Find index of an element:
        - Find the index of the element 4 in the tuple: tuple.index(4)
        - Output: 3
Other important tuple methods:
    - tuple.__add__(other): Concatenates two tuples.
    - tuple.__contains__(item): Checks if an item is in the tuple.
    - tuple.__getitem__(index): Gets the item at the specified index.
    - tuple.__iter__(): Returns an iterator for the tuple.
    - tuple.__len__(): Returns the length of the tuple.
    - tuple.__mul__(n): Repeats the tuple n times.
    - tuple.__rmul__(n): Repeats the tuple n times.
"""

# Accessing elements
print(tuple[0])  # Output: 1

# Slicing
print(tuple[1:3])  # Output: (2, 3)

# Length of tuple
print(len(tuple))  # Output: 5

# Count occurrences of an element
print(tuple.count(3))  # Output: 1

# Find index of an element
print(tuple.index(4))  # Output: 3


t = (1, 2, 3)
u = (4, 5, 6)

z= t + u*3
print(z)