

print()

# using single for loop
def right_triangle(row):
    for i in range(1,row+1):
        print('*'*i)
        
right_triangle(5)

print()
# using double for loop
def right_tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('*', end='')
        print()
        
        
right_tri(5)