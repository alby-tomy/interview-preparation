# find the missing number between n

li = [1,2,4,5,6,7,8,9,10]
if sum(li) != sum(range(1,11)):
    print('missing number is : ', (sum(range(1,11))-sum(li)))
else:
    print('fine')