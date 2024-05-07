for row in range(5,0,-1):
    for col in range(1,row+1):
        print(col, end="")
        if col < row:
            print("*", end="")
    print()
