for row in range(8):
    for col in range(6):
        if(col==0 or col==5) or(row==3 and(col>0 and col<6)):
            print('* ',end='')
        else:
            print(end='  ')
    print()