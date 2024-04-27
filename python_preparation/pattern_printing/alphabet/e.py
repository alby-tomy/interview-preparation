for row in range(9):
    for col in range(9):
        if (col==0) or ((row==0 or row==4 or row==8) and (col>0 and col<8)):
            print('* ', end='')
        else:
            print(end=' ')
    print()
