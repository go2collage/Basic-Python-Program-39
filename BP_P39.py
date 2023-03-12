# find highest 3 values in a Dictionary

# import lib.
from heapq import nlargest

# Create a dictionary
dict1 = {'a': 705, 'b': 546, 'c': 550, 'd': 400, 'e':250}

print("Dictionary 1 is: ", dict1)

# highest 3 values

three_values = nlargest(3, dict1, key= dict1.get)
print("Three largest values of Dictionary 1 is: ", three_values)

# Thanks for Watching
