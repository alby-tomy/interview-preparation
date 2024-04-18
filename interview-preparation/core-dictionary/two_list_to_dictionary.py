
def list_to_dic(keys, values):
    dictionary = {}
    
    if len(keys) != len(values):
        print("Length miss match")
        return None;
    
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]      
        
    return dictionary
    

num_item = int(input("Enter the number of items : "))
keys = []
values = []

for i in range(num_item):
    key = input(f"Enter the key [{i+1}] : ")
    value = input(f"Enter the value for key[{key}] : ")

    keys.append(key)
    values.append(value)
    
result_dict = list_to_dic(keys, values)
print(result_dict)
