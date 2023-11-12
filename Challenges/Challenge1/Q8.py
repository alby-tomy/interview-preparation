def studentDis(price):
    studentDiscount = 0.10
    discPrice = price*(1-studentDiscount)
    return discPrice

def regularBuyer(price):
    regBuyDis = 0.05
    discPrice = price*(1-regBuyDis)
    return discPrice

actualPrice = 500
stdPrice = studentDis(actualPrice)
finalDisPri = regularBuyer(stdPrice)

print(f"Actual Amount : {actualPrice}\n")
print(f"Student Discount : {stdPrice:.2f}\n")
print(f"Regular Buyer Discount : {finalDisPri:.2f}")
