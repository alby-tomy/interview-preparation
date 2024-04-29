for row in range(9):
    for col in range(7):
        if (row==0 or row==8) or (col==0 or col==6 ):
            print('* ', end='')
        else:
            print(end='  ')
    print()
