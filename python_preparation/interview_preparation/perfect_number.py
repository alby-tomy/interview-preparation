def perfect_squre(number):
    sum = 0
    for i in range(1,number):
        if(number % i == 0):
            sum = sum +i
    if(sum == number):
        print("perfect number ")
    else:
        print("not a perfect number")
        
perfect_squre(28)