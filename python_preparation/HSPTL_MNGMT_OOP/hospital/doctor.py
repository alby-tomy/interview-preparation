class Doctor:
    def __init__(self, doctor_id, name, speciality):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__speciality = speciality
        
    def get_details(self):
        return f"Doctor ID: {self.__doctor_id}, Name: {self.__name}, Specialty: {self.__speciality}"
    
    def update_details(self, name=None, specialty=None):
        if name:
            self.__name = name
        if specialty:
            self.__specialty = specialty
