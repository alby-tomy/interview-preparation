
# lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
# lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# after conversion: 
# lst1: [13, 56, 70] 
# lst2: [28, 66, 31] 

# add the elements of same index [ (lst1[0] + lst2[0]), ..n ]
# [(13+ 28), (56+66) ... ]
# output: [41, 122]

# Company : Wahni IT Solutions

lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# convertion
def string_to_int(con_str):
    if con_str == "one":
        return "1"
    elif con_str == "two":
        return "2"
    elif con_str == "three":
        return "3"
    elif con_str == "four":
        return "4"
    elif con_str == "five":
        return "5"
    elif con_str == "six":
        return "6"
    elif con_str == "seven":
        return "7"
    elif con_str == "eight":
        return "8"
    elif con_str == "nine":
        return "9"
    elif con_str == "zero":
        return "0"
        
# combine element in the list
def after_convertion(lis):
    list_tmp = []
    for sublist in lis:
        temp_str = ""
        for item in sublist:
            temp_str += string_to_int(item)
        list_tmp.append(int(temp_str))
    return list_tmp


lst1_con = after_convertion(lst1)
lst2_con = after_convertion(lst2)


# final addition
new_lst = [lst1_con[i] + lst2_con[i] for i in range(len(lst1_con))]
    
print(new_lst)



# Dictionary Conversion
# Define the conversion dictionary
conversion_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}

# Combine elements in the list
def after_conversion(lis):
    list_tmp = []
    for sublist in lis:
        temp_str = ""
        for item in sublist:
            temp_str += conversion_dict[item]
        list_tmp.append(int(temp_str))
    return list_tmp

# Define the input lists
lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# Convert the lists
lst1_con = after_conversion(lst1)
lst2_con = after_conversion(lst2)

# Add the corresponding elements of the converted lists
new_lst = [lst1_con[i] + lst2_con[i] for i in range(len(lst1_con))]

# Print the result
print(new_lst)


# Using List Comprehension and Map
# Define the conversion dictionary
# 'conversion_dict'
  
# Convert sublist to integer
def convert_sublist(sublist):
    return int("".join(map(lambda x: conversion_dict[x], sublist)))

# Define the input lists
lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# Convert the lists using list comprehension and map
lst1_con = [convert_sublist(sublist) for sublist in lst1]
lst2_con = [convert_sublist(sublist) for sublist in lst2]

# Add the corresponding elements of the converted lists
new_lst = [lst1_con[i] + lst2_con[i] for i in range(len(lst1_con))]

# Print the result
print(new_lst)


# Using Zip for Parallel Processing
# You can use zip to iterate over both lists in parallel.
# Define the conversion dictionary
# 'conversion_dict'


# Convert sublist to integer
def convert_sublist(sublist):
    return int("".join(conversion_dict[item] for item in sublist))

# Define the input lists
lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# Convert and add the lists using zip and list comprehension
new_lst = [convert_sublist(sub1) + convert_sublist(sub2) for sub1, sub2 in zip(lst1, lst2)]

# Print the result
print(new_lst)


# Using Numpy for Vectorized Operations
# If performance is a concern, and you have large datasets, you might want to use numpy for vectorized operations.
import numpy as np

# Define the conversion dictionary
# 'conversion_dict'


# Convert sublist to integer
def convert_sublist(sublist):
    return int("".join(conversion_dict[item] for item in sublist))

# Define the input lists
lst1 = [["one", "three"], ["five", "six"], ["seven", "zero"]]
lst2 = [["two", "eight"], ["six", "six"], ["three", "one"]]

# Convert the lists to numpy arrays
lst1_con = np.array([convert_sublist(sublist) for sublist in lst1])
lst2_con = np.array([convert_sublist(sublist) for sublist in lst2])

# Add the corresponding elements of the arrays
new_lst = lst1_con + lst2_con

# Print the result
print(new_lst)
