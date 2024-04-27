def reverse_pyramid(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end=' ')
        for j in range(0,i):
            print('*', end=' ')
        print()

reverse_pyramid(5)

n=5
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))
