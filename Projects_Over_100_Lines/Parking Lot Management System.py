
parking_slots = {
    "p1" : None,
    "p2" : None,
    "p3" : None,
    "p4" : None,
    "p5" : None
}


def park_vehicle():
    vehicle_number = input("Enter Vehicle Number:")
    vehicle_type = input("Enter Vehicle Type:")
    
    for slot, details in parking_slots.items():
        
        if details is None:
            parking_slots [slot] = {
                "vehicle_number": vehicle_number,
                "vehicle_type" : vehicle_type
            }
            
            print("\n Vehicle Parked Successfully!")
            print(f"Parking Slot : {slot}")
            print(f"Veicle Number : {vehicle_number}")
            print(f"Vehicle Type : {vehicle_type}")
            print("-----------------------------------")
            
            break
        
        else:
            print("\n Parking Lot is Full!")
            
            
def view_parking_slots():
    
    print("===== PARKING DETAILS =====")
    
    for slot, details in parking_slots.items():
    
        if details is None:
            print(f"{slot} : Empty")
        
        else:
            print(f"{slot} : Occupied")
            print(f" Vehicle Number : {details['vehicle_number']}")
            print(f" Vehicle Type : {details['vehicle_type']}")
        
    print("---------------------------------------")
    
    
def search_vehicle():
    vehicle_number = input("Enter Vehicle Number:")
    
    for slot, details in parking_slots.items():
        
        if details is not None:
            
            if details["vehicle_number"] == vehicle_number:
                
                print("\n -----VEHICLE FOUND-----")
                print(f"Parking Slot : {slot}")
                print(f"vehicle_number : {details['vehicle_number']}")
                print(f"vehicle_type : {details['vehicle_type']}")
                print("\n---------------------------------")
                
                return
    else:
        print("\n Vehicle Not Found!")
                