my_tuple = (1,2,3,4,5,6,7,8,8,7,4,5)
print(my_tuple)

print()
for i in range(len(my_tuple)):
    print(my_tuple[i],end=" ")
  
print()  
a,b,*c = my_tuple
print(a)
print(b)
print(c)

