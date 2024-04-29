import math

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def print_prime_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(i):
            while not is_prime(num):
                num += 1
            print(num, end=' ')
            num += 1
        print()

# Example usage:
print_prime_pattern(5)
