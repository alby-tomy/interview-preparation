num =0
for i in range(15):
    if i %3 ==0 or i%5==0:
        print(i, 'number that is divisible by 5 or 3')
        num += i 
print(num, 'Total for numbers in range 15 divisible by 3 or 5')

