
print()
for row in range(8):
    for col in range(6):
        if (col==0 and row!=0) or (row==0 or row==7) or(col==5 and(row>3 and row<8)) or (row==4 and(col>3 and col<6)):
            print('* ',end='')
        else:
            print(end='  ')
    print()