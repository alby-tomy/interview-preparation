for row in range(8):
    for col in range(6):
        if(col ==4 and(row!=0)) or (col==0 and (row>3 and row<8)) or (row==0) or (row==7 and(col>0 and col<4)):
            print('* ',end='')
        else:
            print(end='  ')
    print()