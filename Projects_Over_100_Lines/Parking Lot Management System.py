
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