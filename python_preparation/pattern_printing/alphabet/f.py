for row in range(8):
    for col in range(6):
        if (col==0) or (row==0 and (col>0 and col<5)) or (row==4 and(col>0 and col<4)):
            print('* ',end='')
        else:
            print(end='  ')
    print()