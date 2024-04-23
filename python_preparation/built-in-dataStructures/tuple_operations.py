# Creating a tuple
my_tuple = (1, 2, 3, "hello", (4, 5))

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: hello
print(my_tuple[-1]) # Output: (4, 5)

# Tuple unpacking
x, y, z, message, inner_tuple = my_tuple
print(x)           # Output: 1
print(message)     # Output: hello
print(inner_tuple) # Output: (4, 5)

# Immutability
# Trying to modify a tuple will raise an error
# my_tuple[0] = 10  # This will raise TypeError

# Length of tuple
print(len(my_tuple))  # Output: 5

# Tuple with one element (singleton tuple)
singleton_tuple = (42,)
print(singleton_tuple)  # Output: (42,)

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()
