def even_printing(n):
    k = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            print(k, end='')
        k = k+2
        print()

even_printing(5)

