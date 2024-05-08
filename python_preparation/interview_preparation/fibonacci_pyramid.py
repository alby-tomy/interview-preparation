# def fibonacci_pyramid(rows):
#     a,b = 0,1
#     for i in range(rows):
#         print(" "* (rows-i), end="")
        
#         for j in range(i+1):
#             print(a, end=" ")
#             a,b, = b,a+b
#         print()
        
# fibonacci_pyramid(5)

# recurssion method
def fabi_rec(nu):
    if nu <= 1:
        return 1
    else:
        return fabi_rec(nu-1) + fabi_rec(nu-2)
    
num_r = 10
for i in range(num_r):
    print(fabi_rec(i), end=" ")
print()