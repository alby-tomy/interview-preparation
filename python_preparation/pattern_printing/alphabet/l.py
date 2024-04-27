for row in range(8):
    for col in range (6):
        if(col==0) or (row==7):
            print('* ',end='')
        else:
            print(end='  ')
    print()
