# def fabonacci(rangeo:int):
#     i = 0
#     first_val = 0
#     sec_val = 1
    
#     while(i<rangeo):
#         if(i <= 1):
#             next = i
#         else:
#             next = first_val + sec_val
#             first_val = sec_val
#             sec_val = next
#         print(next)
#         i = i+1
        
# fabonacci(10)


# recursion method
def fibrec(num):
    if num == 0:
        return 0
    elif(num == 1):
        return 1
    else:
        return(fibrec(num-2)+fibrec(num-1))

for n in range(10):
    print(fibrec(n))