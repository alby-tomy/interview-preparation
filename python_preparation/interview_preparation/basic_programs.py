# creating list
my_list1 = [1,2,34,4,5,6,7,8]
print(my_list1[0])  # accessing values
print(my_list1)     # to print all elements in the list



# creating dictionary
my_dict = {
    'name':'Anaina',
    'age':32,
    1:'Position'
}

print(my_dict['name'])  # accessing values
print(my_dict[1])




#creating a set
setA = {2,3,4,5,6}

# set operation
setB = {5,6,7,8}
print(setA.union(setB))  # union give elements present in both elements without duplicates
print(setA.intersection(setB)) #Returns common elements between the two sets
print(setA.difference(setB)) #Returns elements that are in setA but not in setB.




# tuple
# creating tuple
my_tuple = (2,3,4,5,6,7)
print(my_tuple[0]) #accessing elements



# basic program
# factorial of fiven number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*factorial(n-1))   #here used recursive function
print(factorial(10))



# string
a = "Birthday"
print(a[-1]) #will access the last element
print(a[0]) #access the first element
print(a[1])

print(a[1:6:2]) # access char from index 1 to 6 by skipping 2 elements
print(a[0:6]) # access from begining till 6th index
print(a[4:]) # accessing from 4th index till end
print(a[::]) # accessing from begining till end
print(a[::-1]) #accessing element from begining till end but in reverse 

# revering given number
# method 1 taking input_as interger
input_num = int(input("Enter number to reverse : ")) #take as int from user
int_to_str = str(input_num) # convert to string
reversed_num = int_to_str[::-1] #use slicing method to reverse slicing symtax [start:stop:step] here [::-1], - or negative used to call the last element
print(reversed_num)

# method to by default the input is string type
input_num2 = input("Enter number to reverse : ")
print(input_num2[::-1])


# removing duplicate elements from list without using set

list1 = [2,2,3,4,5,6,6,5,7]

# method 1 
result_lst = []
duplicate = []

for i in list1:
    if i not in result_lst:
        result_lst.append(i)
    else:
        duplicate.append(i) # to print the duplicate element

print("removed the duplcate : ",result_lst)
print("Duplicated element : ",duplicate)   



# removing duplicate elements from list using set
list12 = [3,4,5,6,5,6,7,7,8]
print(set(list1)) # because set can only have unique values


# swapping two number without using temp variable
# method 1
a=5
b=6
a,b = b,a
print("method 1 :",a,b)


#method 2
a=10
b=12
a = a+b
b = a-b
a = a-b
print("method 2 :",a,b)