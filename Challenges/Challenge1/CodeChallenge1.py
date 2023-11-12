def numToMonth(a):
    if(a == 1):
        print("January")
    elif(a == 2):
        print("Feb")
    elif(a == 3):
        print("March")
    elif(a == 4):
        print("April")
    elif(a == 5):
        print("May")
    elif(a==6):
        print("June")
    elif(a==7):
        print("July")
    elif(a==8):
        print("August")
    elif(a==9):
        print("September")
    elif(a==10):
        print("October")
    elif(a==11):
        print("November")
    elif(a==12):
        print("December")
    else:
        print("Invalid Input")

a = int(input("Enter  digit etween 1 - 12 to find corresponding month : "))
numToMonth(a)
