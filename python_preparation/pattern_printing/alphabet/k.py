
i=0
j=4

for row in range(8):
    for col in range(6):
        if (col==0) or (row==col+3):
            print('* ',end='')
        elif(row==i and col==j):
            print('* ',end='')
            i +=1
            j -=1
        else:
            print(end='  ')
    print()