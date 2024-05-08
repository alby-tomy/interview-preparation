def common_letters():
	str1 = input("Enter string 1 : ")
	str2 = input("Enter string 2 : ")

	s1 = set(str1)
	s2 = set(str2)

	lst = s1 & s2
	print(lst)

common_letters()
