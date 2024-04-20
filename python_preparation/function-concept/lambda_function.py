# Lambda Function
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_list = sorted(original_list, key=lambda x: x[1])
print("Sorted list of tuples:")
print(sorted_list)


# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
# 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dictionary_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color':
'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sort_list = sorted(dictionary_list, key=lambda x:x['make'])
print("Sorted list of tuples : ")
print(sort_list)

# Write a Python program to square and cube every number in a given list of integers
# using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = list(map(lambda x: x**2, int_list))
cubed_list = list(map(lambda x:x**3, int_list))
print("Original list of integers:", int_list)
print("Squared list:", square_list)
print("Cubed list:", cubed_list)


# Write a Python program to create Fibonacci series up to n using Lambda.
# Function to generate Fibonacci series up to n terms
fibonacci = lambda n: [0, 1] + [sum(fib[-2:]) for fib in [fibonacci(i) for i in range(2, n)]]
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci_series = fibonacci(n)
print("Fibonacci series up to", n, "terms:", fibonacci_series)

# Write a Python program to find numbers divisible by nineteen or thirteen from a list
# of numbers using Lambda.
numbers = [19, 13, 25, 38, 39, 52, 65, 76, 91, 95]
divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print("Numbers divisible by nineteen or thirteen:", divisible_by_19_or_13)


# Write a Python program to calculate the sum of the positive and negative numbers
# of a given list of numbers using the lambda function.
numbers = [-10, 5, -8, 12, -3, 7, -15, 20]
# Calculate the sum of positive numbers using a lambda function with filter()
sum_positive = sum(filter(lambda x: x > 0, numbers))
# Calculate the sum of negative numbers using a lambda function with filter()
sum_negative = sum(filter(lambda x: x < 0, numbers))
print("Sum of positive numbers:", sum_positive)
print("Sum of negative numbers:", sum_negative)