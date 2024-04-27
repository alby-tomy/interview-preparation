for row in range(8):
    for col in range(3):
        if(col==1) or (row==0 or row==7):
            print('* ',end='')
        else:
            print(end='  ')
    print()