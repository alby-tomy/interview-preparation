# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Accessing elements
print(my_dict["name"])  # Output: John

# Modifying elements
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding new elements
my_dict["gender"] = "Male"
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'gender': 'Male'}

# Removing elements
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'gender': 'Male'}

# Checking for key existence
if "name" in my_dict:
    print("Name is present.")  # Output: Name is present.

# Looping through key-value pairs
for key, value in my_dict.items():
    print(key, ":", value)
# Output:
# name : John
# age : 31
# gender : Male
