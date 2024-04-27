def diamond(n):
    # Upper half of the diamond
    for i in range(n):
        print(" " * (n-i-1) + "* " *(i+1))
    
    # Lower half of the diamond
    for i in range(n-1,0,-1):
        print(" " * (n-i) + "* " *(i))

diamond(5)

