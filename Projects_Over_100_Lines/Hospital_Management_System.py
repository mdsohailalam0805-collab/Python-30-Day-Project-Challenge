
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



    