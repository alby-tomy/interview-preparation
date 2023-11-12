def zeroDivisionChecker(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print("Error : ",e)


a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

zeroDivisionChecker(a,b)
