class Person(object):
    
    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum
        
    def display(self):
        print(self.name)
        print(self.idnum)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("My id is : {}".format(self.idnum))
        
class Employee(Person):
    def __init__(self, name, idnum, salary, post):
        self.salary = salary
        self.post = post
        
        Person.__init__(self, name, idnum)
        
    def details(self):                              # override
        print("My name is {}".format(self.name))
        print("Idnumber : {}".format(self.idnum))
        print("Post : {}".format(self.post))
       
       
        
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()