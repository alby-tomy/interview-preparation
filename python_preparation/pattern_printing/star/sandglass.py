for row in range(10):
    for j in range(0,row):
        print(end=" ")
    for k in range(row,10):
        print("*",end=" ")
    print()

for row in range(9, -1, -1):
    for j in range(0,row):
        print(end=" ")
    for k in range(row, 10):
        print("*", end=" ")
    print()

