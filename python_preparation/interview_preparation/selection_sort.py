data_sort = [5,6,4,2,31,9,8,10]

leng = len(data_sort)
res = []

for i in range(leng):
    for j in range(i+1, leng):
        if data_sort[j] < data_sort[i]:
            data_sort[i], data_sort[j] = data_sort[j], data_sort[i]
            
print(data_sort)