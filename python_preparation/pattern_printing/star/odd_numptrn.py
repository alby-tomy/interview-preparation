def odd_num_ptrn(n):
    num = 1
    for i in range(n):
        for j in range(i):
            print(num, end=' ')
            num +=2
        print()

odd_num_ptrn(5)

