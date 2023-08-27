# Lists and collections
# Arrays consists of only numeric data types and every element has to be of the same data type
# Lists can store any data type giving more flexibility

# Lists are collections of items
names = ["Christopher", "Susan"]
scores = []
scores.append(98) # Adds new items to the list
scores.append(99)

print(names)
print(scores)
print(scores[1])
print()
# Arrays are also collections of items
from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])
print()

# Common operations
print(len(names)) # Get the number of items
names.insert(0, "Bill") # Insert before the index

print(names)
print()
names.sort()
print(names)