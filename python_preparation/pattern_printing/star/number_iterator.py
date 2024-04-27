def number_ittr(n):
    for i in range(n):
        for j in range(i):
            print(i, end=' ')
        print()

number_ittr(6)
