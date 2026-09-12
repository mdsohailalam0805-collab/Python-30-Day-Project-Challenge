
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
        print("Patient Not Found!")
        return
    
    for patient_id, details in patients.items():
        
        print("------PATIENT DETAILS------")
        
        print(f"Patient Id: {patient_id}")
        print(f"Patient Name : {details['patient_name']}")
        print(f"Age : {details['age']}")
        print(f"Disease : {details['disease']}")  
        
        print("---------------------------------") 
        
view_patient()

        
    