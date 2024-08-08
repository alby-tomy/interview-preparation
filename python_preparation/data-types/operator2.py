# How to find duplicate and missing elements? (Eg 1,3,3,4,5 and sum = 2+3=5)


lst = [1,3,3,4,5]
for i in range(len(lst)):
    for  j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            du = lst[j]
print(du)


# Calculate the sum of the elements in the list
p_sum = sum(lst)
n = len(lst)

# Calculate the expected sum of numbers from 0 to len(lst)
mis_num = sum(range(1,n+1)) - (p_sum - du)
print(mis_num)