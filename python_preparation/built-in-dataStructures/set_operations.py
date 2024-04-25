# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Adding elements to a set
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding duplicate elements (ignored)
my_set.add(3)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing elements from a set
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4}

# Intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {2, 3}

# Difference
difference_set = set1 - set2
print(difference_set)  # Output: {1}

# Symmetric difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 4}
