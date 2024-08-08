def mystery_function(n, lst=None):
    if lst is None:
        lst = []
        
    if n <= 1:
        lst.append(n)
        return lst
    else:
        mystery_function(n - 1, lst)
        mystery_function(n - 2, lst)
        lst.append(lst[-1] + lst[-2])
        return lst

lst = mystery_function(5)
print(lst)
