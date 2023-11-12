class Hospital:
    def __init__(self,admin,doc,sister,department):
        self.admin = admin
        self.doc = doc
        self.sister = sister
        self.department = department

    def departmentD(self):
        self.admin = input("Enter Admin's Name : ")
        self.doc = input("Enter Doctor's Name : ")
        self.sister = input("Enter the Sister's Name : ")
        self.department = input("Department : ")

    def getDetails(self):
        print("\nAdmin : {}\nDoctor : {}\nSister : {}\nDepartment : {}\n".format(self.admin,self.doc,self.sister,self.department))

class PatientDetails(Hospital):
    def __init__(self, name,age,number,disease):
        self.name = name
        self.age = age
        self.number = number
        self.disease = disease

    def patientD(self):
        self.name = input("Patient Name : ")
        self.age = input("Age : ")
        self.number = input("Number : ")
        self.disease = input("Disease : ")

    def printPatD(self):
        print("\nName : {}\nAge : {}\nNumber : {}\nDisease : {}".format(self.name,self.age,self.number,self.disease))



obj = PatientDetails('','','','')
obj.departmentD()
obj.patientD()
print("\n\nDetails Printing")
obj.getDetails()
obj.printPatD()
