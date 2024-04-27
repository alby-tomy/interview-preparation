
i=2
j=4

for row in range(8):
    for col in range(7):
        if(col==0 or col==6) or (row==col and (row <4 and col <4)) or (col==4 and row==2) or (col==5 and row==1):
            print('* ',end='')
            
            
        else:
            print(end='  ')
    print()