def fibonacci_pyramid(rows):
    a,b = 0,1
    for i in range(rows):
        print(" "* (rows-i), end="")
        
        for j in range(i+1):
            print(a, end=" ")
            a,b, = b,a+b
        print()
        
fibonacci_pyramid(5)