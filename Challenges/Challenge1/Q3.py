def finalP(pro_PrizeX, pro_PrizeY):
    return (pro_PrizeX/pro_PrizeY ** 2)

x_prize = int(input("Enter the price for X : "))
y_prize = int(input("Enter the price for Y : "))
a = finalP(x_prize, y_prize)
print(a)
