
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

def view_patient():
    
    if not patients:
        print("Patient Not Available!")
        
        return
    
    for patient_id, details in patients.items():
        
        print("------ALL PATIENT DETAILS------")
        
        print(f"Patient Id: {patient_id}")
        print(f"Patient Name : {details['patient_name']}")
        print(f"Age : {details['age']}")
        print(f"Disease : {details['disease']}")  
        
        print("---------------------------------") 


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


appointments = {}

def book_appointment():
    patient_id = input("Enter Patient Id:")
    
    if patient_id not in patients:
        print("\nPatient Not Found!")
        return
    
    doctor_id = input("Enter Doctor Id:")
    
    if doctor_id not in doctors:
        print("\n Doctor Not Found!")
        return
    
    appointment_date = input("Enter Appointment Date:")
    
    appointments[patient_id] = {
        "doctor_id" : doctor_id,
        "appointment_date" :appointment_date
    }
        
    print("\n Appointment Booked Successfully!")
    print("--------------------------------------")
    

def generate_bill():
    patient_id = input("Enter patient Id:")
    
    if patient_id not in patients:
        print("\n Patient Not Found!")
        return
    
    consultation_fee = float(input("Enter Consultation Fee:"))
    medicine_charges = float(input("Enter Medicine Charges:"))
    
    total_bill = consultation_fee + medicine_charges
    
    print("\n------HOSPITAL BILL------")
    
    print(f"Patient Id : {patient_id}")
    print(f"Patient Name : {patients[patient_id]['patient_name']}")
    print(f"Consultation Fee : {consultation_fee}")
    print(f"Medicine Charges : {medicine_charges}")
    
    print(f"Total Bill : {total_bill}")
    print("-----------------------------------------")
    

def delete_patient():
    patient_id = input("Enter Patient Id to delete:")
    
    if patient_id in patients:
        del patients[patient_id]
        
        print("\n Patient Deleted Successfully!")
        print("----------------------------------")
        
    else:
        print("\nPatient Not Found!")    
        

def main_menu():
    
    while True:
        
        print("1. Add patient")
        print("2. View Patient")
        print("3. Search patient")
        print("4. Add Doctor")
        print("5. Book Appointment")
        print("6. Generate_Bill")
        print("7. Delete Patient")
        print("8. Exit")
        
        choice = input("Enter Your Choice:")
        
        if choice == "1":
            add_patients()
            
        elif choice == "2":
            view_patient()
            
        elif choice == "3":
            search_patient()
            
        elif choice == "4":
            add_doctor()
            
        elif choice == "5":
            book_appointment()
            
        elif choice == "6":
            generate_bill()
            
        elif choice == "7":
            delete_patient()
            
        elif choice == "8":
            print("\n Thank You For Using Hospital Management System.")
            break
        
        else:
            print("Invalid choice , Please Try Again!")
            
main_menu()