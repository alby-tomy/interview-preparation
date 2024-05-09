my_list = [1,2,3,5,6,7,8,8,7,9]
for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] + my_list[j] == 10:
            print("Hello World : " +str(my_list[i]) + " and " + str(my_list[j]))
            
        if my_list[i] + my_list[j] == 5:
            temp = my_list[i]+my_list[j] + 10
            print("appended ",my_list.append(temp))
            print("insert : ",my_list.insert(2, temp))
            my_list.remove(5)
            print(my_list)
            print(my_list)
            print("sorted : ", my_list.sort())
            
subset = my_list[1:6]
print(subset)

squares = [subset[x]**2 for x in range(0, len(subset))]
print(squares)