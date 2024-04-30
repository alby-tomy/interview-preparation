def calculate_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return calculate_binomial_coefficient(n - 1, k - 1) + calculate_binomial_coefficient(n - 1, k)

def print_pascals_triangle(rows):
    for i in range(rows):
        # for j in range(rows - i - 1):
        #     print(" ", end=" ")
        for j in range(i + 1):
            print(calculate_binomial_coefficient(i, j), end=" ")
        print()

# Example usage:
print_pascals_triangle(5)
