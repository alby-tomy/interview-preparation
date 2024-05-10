list_d = [5,4,3,7,6,2]


leng = len(list_d)
for i in range(leng):
    for j in range(leng-i-1):
        if list_d[j+1] < list_d[j]:
            list_d[j+1], list_d[j] == list_d[j], list_d[j+1]

print(list_d)