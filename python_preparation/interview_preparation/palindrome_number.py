def palin(n):
    v = str(n)
    if v == v[::-1]:
        return True
    else:
        return False
    
print(palin(1121))