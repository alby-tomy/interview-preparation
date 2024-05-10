my_set = {2,2,4,5,6,8,9,1,2,3,8}

print(my_set)
for i in my_set:
    print(i)
    
    if i == 6:
        my_set.add(123)
        my_set.remove(3)
    
    set2 = set()
    if i%2 == 0:
        set2.add(i)
        
        union = my_set.union(set2)
        print(union)
        print(set2)