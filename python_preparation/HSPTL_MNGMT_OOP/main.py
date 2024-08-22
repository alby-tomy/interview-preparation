from hospital import Hospital, Patient, Doctor, Appoinment

# create hospital
hospital = Hospital("City Hospital")


# create doctor
doctor1 = Doctor(1, "Dr. XYZ1", "ASDFG")
doctor2 = Doctor(2, "Dr. XYZ2", "ASDFG")
doctor3 = Doctor(3, "Dr. XY3", "ASDFG")
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)
hospital.add_doctor(doctor3)


# create patients
patient1 = Patient(1, "ABC1", 30, "M")
patient2 = Patient(2, "ABC2", 31, "F")
patient3 = Patient(3, "ABC3", 32, "M")
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.add_patient(patient3)





# Book appoinment
appointment1 = Appoinment(1, patient1, doctor1, "2024-08-23")
appointment2 = Appoinment(2, patient2, doctor2, "2024-08-24")
hospital.book_appointment(appointment1)
hospital.book_appointment(appointment2)


# display
hospital.show_all_patients()
hospital.show_all_doctors()
hospital.show_all_appointments()