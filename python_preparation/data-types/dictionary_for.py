dic = {'a':1,'b':23,'c':34,'d':45}

for key in dic:
    print(key)
    
# Iteration over value
for value in dic.values():
    print(value)
    
# Iteration over key-value pair
for key,value in dic.items():
    print(f"{key} : {value}")
    
dic = {'a':1,'b':23,'c':34,'d':45}

print(dic['a'])
