class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        
    def get_details(self):
        return f"Patient ID: {self.__patient_id}, Name: {self.__name}, Age: {self.__age}, Gender: {self.__gender}"
    
    def update_details(self, name = None, age=None, gender=None):
        if name:
            self.__name = name
        if age:
            self.__age = age
        if gender:
            self.__gender = gender
