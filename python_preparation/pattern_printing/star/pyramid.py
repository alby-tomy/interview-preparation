def print_pyramid(rows):
    for i in range(rows):
        print(" " *(rows-i)+ "*" * (2 * i+1))
        
        
# Example usage:
rows = 5
print_pyramid(rows)
def diamond_ptrn(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(end=' ')
        for j in range(0,i+1):
            print('*', end=' ')
        print()


print()


n = 5
for i in range(0,n):
    print(' '*(n-i-1)+'*'*(2*i+1))

diamond_ptrn(5)
