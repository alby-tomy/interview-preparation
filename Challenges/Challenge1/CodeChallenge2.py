def simpleInterest(p,r,t):
    return ((p*r*t)/100)

p = int(input("Enter the principle amount : "))
r = int(input("Enter the rate : "))
t = int(input("Enter the time period in years : "))

ans = simpleInterest(p,r,t)
print(ans)
