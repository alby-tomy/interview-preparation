list2 = [2, 5, 7, 6, 8, 4, 5, 6, 7, 6, 5, 9, 11]

empty_list = []

for element in list2:
    if element not in empty_list:
        empty_list.append(element)
        
print(empty_list)
pairs  = set()

for i in range(len(list2)):
    for j in range(1,len(list2)):
        if list2[i]+list2[j] == 12:
            pairs.add((list2[i],list2[j]))
            
for pair in pairs:
    print(pair)