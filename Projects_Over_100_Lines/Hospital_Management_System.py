
patients = {}

def add_patients():
    patient_id = input("Enter patient Id:")
    patient_name = input("Enter patient Name:")
    age = int(input("Enter patient Age:"))
    disease = input("Enter disease:")
    
    patients[patient_id] = {
        
        "patient_name" : patient_name,
        "age" : age,
        "disease" : disease 
        
    }
    
    print("\n Patient Added Successfully:")
    print("---------------------------------")

add_patients()   
print(patients)


def view_patient():
    patient_id = input("Enter patient Id:")
    
    if patient_id not in patients:
        print("Patient Not Available!")
        return
    
    for patient_id, details in patients.items():
        
        print("------PATIENT DETAILS------")
        
        print(f"Patient Id: {patient_id}")
        print(f"Patient Name : {details['patient_name']}")
        print(f"Age : {details['age']}")
        print(f"Disease : {details['disease']}")  
        
        print("---------------------------------") 
        
view_patient()


def search_patient():
    patient_id = input("Enter patient Id:")
    
    if patient_id in patients:
        details = patients[patient_id]
        
        print("\n ------PATIENT DETAILS------")
        
        print(f"Patient Id : {patient_id} ")
        print(f"Patient Name : {details['patient_name']}")
        print(f"Age : {details['age']}")
        print(f"Disease : {details['disease']}")
        print("-----------------------------------")
        
    else:
        print("\n Patient Not Found!")
        
search_patient() 
 
        
doctors = {}

def add_doctor():
    doctor_id = input("Enter Doctor Id:")
    doctor_name = input("Enter Doctor Name:")
    specialization = input("Enter Doctor Specialization:")
    
    doctors[doctor_id] = {
        
        "doctor_name" : doctor_name,
        "specialization" : specialization
        
    }
    print("\n Doctor Added Successfully!")
    print("---------------------------------")
    
    