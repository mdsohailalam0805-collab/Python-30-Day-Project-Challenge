bookings = {}

def booking_room():
    
    room_number = input("Enter Room Number:")
    guest_name = input("Enter Guest Name:")
    days = int(input("Enter Number of Days:"))
    room_price = float(input("Enter Room Price Per Days:"))
    
    bookings[room_number] = {
        "guest_name" : guest_name,
        "days" : days,
        "room_price" : room_price
    }
    
    print("\n Room Booked Successfully!")
    

def view_booking():
    
    if not bookings:
        print("\n No Booking Available!")
        
        print("\n ===== ALL BOOKINGS =====")
        
        for room_number, details in bookings.items():
            
            print(f"Room Number : {room_number}")
            print(f"Guest Name : {details['guest_name']}")
            print(f"Days : {details['days']}")
            print(f"Room Price : {details['room_price']}")
            print("---------------------------------------")
            

def search_booking():
    room_number = input("Enter Room Number:")
    
    if room_number in bookings:
        details = bookings[room_number]
        
        print("\n ===== BOOKING DETAILS =====")
        
        print(f"Room Number : {room_number}")
        print(f"Guest name : {details['guest_name']}")
        print(f"Days : {details['days']}")
        print(f"Room Price : {details['room_price']}")
        print("---------------------------------------")
        
    else:
        print("\n Booking Not Found!")
        

def calculate_bill():
    room_number = input("Enter Room Number:")
    
    if room_number in bookings:
        details = bookings[room_number]
        
        total_bill = details["days"] * details["room_price"]
        
        print("\n ===== BILL DETAILS =====")
        
        print(f"Room Number : {room_number}")
        print(f" Guest Name : {details['guest_name']}")
        print(f" Days : {details['days']}")
        print(f" Room Price : {details['room_price']}")
        
    else:
        print("\n Booking Not Found!")
        
        
def update_booking():
    room_number = input("Enter Room Number:")
    
    if room_number in bookings:
        details = bookings[room_number]
        
        new_guest_name = input("Enter new guest name:")
        new_days = int(input("Enter new days:"))
        new_price_room = input("Enter new price Room:")
        
        details["guest_name"] = new_price_room
        details["days"] = new_days
        details["room_price"] = new_price_room
        
        print("\n Booking Updated Successfully!")
        print("-----------------------------------")
        
    else:
        print("\n Bookings Not Found!")
        print("------------------------")


def cancel_booking():
    room_number = intput("Enter Room Number:")
    
    if room_number in bookings:
        del bbookings[room_number]
        
        print("\n Booking Cancel successfully!")
        print("----------------------------------")
        
    else:
        print("\n Booking not Found!")
        
        
def main_menu():
     while True:
         
         print("\n ===== HOTEL MANAGEMENT SYSTEM =====")
         print("1. Booking Room")
         print("2. View Booking")  
         print("3. Search Booking")
         print("4. Calculate Bill")
         print("5. Update Booking")
         print("6. Cancel Booking")
         print("7. Exit")
         
         choice = input("Enter Your Choice:")
         
         if choice == "1":
             booking_room()
             
         elif choice == "2":
             view_booking()
             
         elif choice == "3":
             search_booking()
             
         elif choice == "4":
             calculate_bill()
             
         elif choice == "5":
             update_booking()
             
         elif choice == "6":
             cancel_booking()
             
         elif choice == "7":
             print("\n Thank You For Using HOTEL MANAGEMENT SYSTEM!")
             
             break
         
         else:
             print("\n Invalid Choice ! Please Try Again.")

main_menu()
                           