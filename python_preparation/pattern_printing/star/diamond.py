def diamond(n):
    for i in range(0,n):
        for j in range(n-i):
            print(end=' ')
        for j in range(i):
            print('*', end=' ')
        print()
    for i in range (n,0,-1):
        for j in range(n-i):
            print(end=' ')
        for j in range(i):
            print('*',end=' ')
        print()

diamond(5)
