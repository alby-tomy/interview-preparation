def amstrong(number: int):
   s = str(number)
   while len(s) < 1:
      return 0
   
   total = 0
   
   for i in s:
      total = total + int(i) ** len(s)
   if total == number:
      return ("Its Amstrong")
   else:
      return ("Not an Amstrong")
      
print(amstrong(259))