sort_data = [8,9,5,6,1,2,3,4,5,10]

leng = len(sort_data)
for i in range(leng):
    key = sort_data[i]
    
    j = i-1
    while(j>=0 and key < sort_data[j]):
        sort_data[j+1] = sort_data[j]
        j -= 1
    sort_data[j+1] = key
        
        
print(sort_data)  