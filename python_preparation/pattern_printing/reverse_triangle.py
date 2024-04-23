def reverse_tri_ptrn(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=' ')
        print()
        
reverse_tri_ptrn(5)