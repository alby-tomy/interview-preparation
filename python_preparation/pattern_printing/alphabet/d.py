for row in range(9):
    for col in range(7):
        if (col==0) or (col==6 and (row!=0 and row!=8)) or ((row==0 or row==8)and (col>0 and col<6)):
            print('* ', end='')
        else:
            print(end='  ')
    print()
