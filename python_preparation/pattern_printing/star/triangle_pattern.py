def triangle_ptrn(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end=' ')
        print()
        
triangle_ptrn(5)