def reverse_pt(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end=' ')
        for j in range(0,i):
            print('*', end=' ')
        print()


reverse_pt(5)


def reverse_ppt(n):
    for i in range(n+1):
        for j in range(0,n-i):
            print(end=' ')
        for j in range(0,i):
            print('*', end=' ')
        print()

reverse_ppt(5)
reverse_pt(5)
