file = open("Fileprogram.txt",'w+')
file.write("ABCDEFGHIJKLMNO PQRSTUVWXYZ")
#file.close()
file.seek(0)

#file = open("Fileprogram.txt",'r')
content = file.readline()
print(content)
file.close()

file = open("Fileprogram.txt",'a')
file.write("\nappended data abcd efghij\n")
file.close()

