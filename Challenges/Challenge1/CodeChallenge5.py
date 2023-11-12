print("\npart a : ")
origiList = [1,2,3,4,5,6,7,8,9]
print("original list :",origiList)
newList = [x+1 for x in origiList]
print("new list : ",newList)

print("\npart b :")
print(origiList[2:6])

print("\npart c :")
tupleData = (1,"A",2,"B",3,4,5,6,7,"C")
print("tuple Data : ",tupleData)
print("to modify values in tuple it should convert to list")

listTuple = list(tupleData)
listTuple.insert(2,10)
listTuple.append(15)
print("\n",listTuple)
print("\n",tupleData[-2])
