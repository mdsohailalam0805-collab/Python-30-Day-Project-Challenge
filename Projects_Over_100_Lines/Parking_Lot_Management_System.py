
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
        
        
def remove_vehicle():
    vehicle_number = input("Enter Vehicle Number:")
    
    for slot, details in parking_slots.items():
        
        if details is not None:
            
            if details["vehicle_number"] == vehicle_number:
                parking_slots[slot] = None
                
                print("\n Vehicle Removed Successfully!")
                print(f"Parking Slot : {slot}")
                print(f"Vehicle Number : {vehicle_number}")
                print(f"Vehicle Type : {details['vehicle_type']}")
                print("-----------------------------------")
                
                return
            
    print("\n Vehicle Not Found!")        
    
    
def calculate_bill():
        vehicle_number = input("Enter Vehicle Number:")
        
        vehicle_found = False
        
        for slot, details in parking_slots.items():
            
            if details is not None:
                
                if details["vehicle_number"] == vehicle_number:
                    vehicle_found = True

                    parking_hours = float(input("Enter parking hours:"))
                    rate_per_hour = 20
                    
                    total_bill = parking_hours * rate_per_hour
                    
                    print("\n===== PARKING BILL =====")
                    print(f"Vehicle Number : {vehicle_number}")
                    print(f"Parking Slot : {slot}")
                    print(f"Parking Hours : {parking_hours}")
                    print(f"Rate Per Hour : ₹{rate_per_hour}")
                    print(f"Total Bill : ₹{total_bill}")
                    print("---------------------------------")
                    
                    return
                
        if not vehicle_found:
            print("\n Vehicle Not Found!") 
                
                
def main_menu():
    
    while True:
        
        print("\n===== PARKING LOT MANAGEMENT SYSTEM =====")
        print("1. Park Vehicle")
        print("2. View Parking Slots")
        print("3. Search Vehicle")
        print("4. Remove Vehicle")
        print("5. Calculate Parking Bill")
        print("6. Exit")
        
        choice = input("Enter Your Choice:")
        
        if choice == "1":
            park_vehicle()

        elif choice == "2":
            view_parking_slots()

        elif choice == "3":
            search_vehicle()

        elif choice == "4":
            remove_vehicle()

        elif choice == "5":
            calculate_bill()

        elif choice == "6":
            print("\nThank You For Using Parking Lot Management System!")
            break

        else:
            print("\nInvalid Choice! Please Try Again!")


main_menu()