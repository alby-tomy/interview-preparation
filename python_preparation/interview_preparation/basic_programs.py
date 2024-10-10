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
# factorial of given number

def get_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*get_factorial(n-1))   # here continuously calling the function that we created [recursive method : calling function itself]
print(get_factorial(10))



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



# Basic of ops
# concepts of oops
# feature of oops
"""
    what is polymorphism ? : Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types 
                            to be treated as if they were of the same type. It enables you to write code that can work with objects of 
                            various classes in a uniform way.
                            
                             
                            
    abstraction : Abstraction is a fundamental concept in object-oriented programming that allows you to focus on the essential features
                of an object while hiding the unnecessary details. It simplifies complex systems by providing a higher-level view. 
                
                
    
    enscapsulation :bundling data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. This helps protect the data from 
                    unauthorized access or modification.
                    
                    
                    
    Inheritance : allows you to create new classes (subclasses) based on existing classes (superclasses). Subclasses inherit the properties and methods of their superclass, 
                    providing a mechanism for code reuse and creating specialized objects.
                    
                    
    
    why python is dynamic? ans : because it can identify the datatypes even without assigning it like a=5
                                    in short AUTOMATIC TYPE IDENTIFICATION, INTERPRETED LANGUAGE 
                                    Python is an interpreted language, which means that the code is executed line by line.
                                    This allows for more flexibility in terms of data types, as the interpreter can handle type conversions and checks at runtime.
    
    
    
    what is decarator? : A decorator in Python is a function that takes another function as an argument and returns a new function. 
                        It's a way to modify or enhance the behavior of existing functions without directly altering their code.
                        starts using double underscore __
                        
                        
    what are magic functions? : functions starts and ends with double underscore eg:__init__, __add__
    
    
    What is a constructor ? : A constructor is a special method in object-oriented programming that is automatically called when an object of a class is created. 
                            Its primary purpose is to initialize the object's attributes or properties.
                            
    What kind of datatypes can be used as keys in dictionary ? ans : Immutable datatypes example string, tuple, int, float
    
    Why string is immutable? : Strings in Python are immutable for several important reasons, primarily related to performance, security, and memory management.
    
    Mjaor difficulties that u faced during your previous project how did you overcome that
    
    Have done any project? Explain the project
    
    
    
    
    # HR common queation
    * ur strength and weakness
    * qualities for a team member
    * if a team member is not able to complete the task in on time, but you want to complete the project on time what will you do....
    * how can you see yourself after 5 years
    * how can you rate yourself in python...
    
    
    """
