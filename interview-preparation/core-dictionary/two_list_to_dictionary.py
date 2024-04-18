def list_to_dic(list1, list2):
    keys = list1
    values = list2
    
    dictionary = {}
    
    if len(keys) != len(values):
        print("Length miss match")
        return None;
    
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
      
    return dictionary
    

num_item = int(input("Enter the number of items : "))
list1 = []
list2 = []

for i in range(num_item):
    key = input(f"Enter the key [{i+1}] : ")
    value = input(f"Enter the value for key[{key}] : ")

    list1.append(key)
    list2.append(value)
    
result_dict = list_to_dic(list1, list2)
print(result_dict)
