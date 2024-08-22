class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []  # Corrected from 'appoinments' to 'appointments'
        
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def book_appointment(self, appointment):  # Corrected spelling
        self.appointments.append(appointment)  # Corrected from 'appoinments' to 'appointments'
        
    def show_all_patients(self):
        for patient in self.patients:
            print(patient.get_details())
            
    def show_all_doctors(self):
        for doctor in self.doctors:
            print(doctor.get_details())
            
    def show_all_appointments(self):  # Corrected method name
        for appointment in self.appointments:  # Corrected from 'self.book_appoinment' to 'self.appointments'
            print(appointment.get_details())
