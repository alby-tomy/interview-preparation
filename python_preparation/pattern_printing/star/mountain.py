def mountain(n):
    for i in range(n):
        print('*'*i+' '*(n-i-1) + ' '*(n-i-1)+'*'*(i))

mountain(10)

