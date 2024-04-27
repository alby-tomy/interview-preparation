i=1
j=1

for row in range(8):
    for col in range(8):
        if (col==0 or col==7):
            print('* ',end='')
        elif(col==i and row==j):
            print('* ',end='')
            i +=1
            j +=1
            
            
        else:
            print(end='  ')
    print() 