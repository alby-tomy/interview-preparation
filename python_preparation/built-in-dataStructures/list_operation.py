# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: 5

# Slicing
print(my_list[1:4]) # Output: [2, 3, 4]
print(my_list[:4]) # Output: [1,2, 3, 4]
print(my_list[:5:2]) # Output: [1,3, 5]

# Modifying elements
my_list[2] = 10
print(my_list) # Output: [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list) # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list) # Output: [1, 10, 4, 5, 6]

# Sorting
my_list.sort()
print(my_list) # Output: [1, 4, 5, 6, 10]

# List comprehension
squared = [x**2 for x in my_list]
print(squared) # Output: [1, 16, 25, 36, 100]
