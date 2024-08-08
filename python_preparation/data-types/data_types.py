
# list operations
lst = [1,2,3,4,5]
lst.append(6)
lst.insert(2,99)
print(lst)

# string manipulation
s = "Hello World"
print(s.lower())
print(s.replace("Hello","Hi"))

# Dictionary
d = {'a':1,'b':2,'c':3}
print(d['a'])
del d['b']
print(d)
bp = d.pop('c')
print(bp)

# Set Operations
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2))

# Tuple Immutability
t = (1,2,3,4)
# t[1] = 45 will raise an error
print(t)


