class Appoinment:
    def __init__(self, appoinment_id, patient, doctor, date):
        self.__appointment_id = appoinment_id
        self.__patient = patient
        self.__doctor = doctor
        self.__date = date
    
    def get_details(self):
        return (f"Appointment ID: {self.__appointment_id}, Patient: {self.__patient.get_details()}, "
                f"Doctor: {self.__doctor.get_details()}, Date: {self.__date}")
    
    def reschedule(self, new_date):
        self.__date = new_date