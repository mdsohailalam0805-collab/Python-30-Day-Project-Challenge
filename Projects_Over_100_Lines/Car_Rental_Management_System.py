# Car Rental Management System

cars = {}

def add_car():
    car_id = input("Enter car id:")
    car_model = input("Enter car Model:")
    price_per_day = float(input("Enter rental price per day:"))
    
    cars[car_id] = {
        "car_model": car_model,
        "price_per_day": price_per_day,
        "status": "Available"
    }
    
    print("\n Car added Successfully!")
    print("-----------------------------")
    
    
def view_cars():
    car_id = input("Enter car id:")
    
    if not cars:
        print("\n No cars available!")
        return
    
    for car_id, details in cars.items():
        
        print(f"Car Id : {car_id}")
        print(f"Car Model : {details['car_model']}")
        print(f"Price Per Day : {details['price_per_day']}")
        print(f"status : {details['status']}")
        
        print("------------------------------------------")
        
        
def search_car():
    car_id = input("Enter car id:")
    
    if car_id in cars:
        details = cars[car_id]
        
        print("\n ----- CAR DETAILS -----")
        print(f"Car Id : {car_id}")
        print(f"Car model : {details['car_model']}")
        print(f"Price Per Day : {details['price_per_day']}")
        print(f"Status : {details['status']}")
        print("------------------------------------------")
        
    else:
        print("\n Car not found!")
        print("------------------------------------------")
        
        
def rent_car():
    car_id = input("Enter car id:")
    
    if car_id in cars:
        details = cars[car_id]
        
        if details["status"] == "Available":
            customer_name = input("Enter customer name:")
            rental_days = int(input("Enter number of rental days: "))

            details["status"] = "Rented"
            details["customer_name"] = customer_name
            details["rental_days"] = rental_days

            
            print("\n Car Rented Successfully!")
            print(f"Car Id : {car_id}")
            print(f"Customer : {customer_name}")
            print("------------------------------------------")
            
        else:
            print("\n Car is already Rented!")
            print("------------------------------------------")
    else:
        print("\n Car not found!")
        print("------------------------------------------")
        
        
def return_car():
    car_id = input("Enter Car id:")
    
    if car_id in cars:
        details = cars[car_id]
        
        if details["status"] == "Rented":
            details["status"] = "Available"
            
            del details["customer_name"]
            
            print("\n Car returned Successfully!")
            print(f"Car Id : {car_id}")
            print(f"Model : {details['car_model']}")
            print(f"status : {details['status']}")
            print("------------------------------------------")
            
        else:
            print("\nThis car is allready available!")
            print("------------------------------------------")
            
    else:
        print("\n Car not Found!")
        print("------------------------------------------")
        
        
def calculate_bill():
    car_id = input("Enter car id:")
    
    if car_id in cars:
        details = cars[car_id]
        
        if details["status"] == "Rented":
            total_bill = details['price_per_day'] * details['rental_days']
            
            print("===== RENTAL BILL =====")
            print(f"Car ID : {car_id}")
            print(f"Customer : {details['customer_name']}")
            print(f"Model : {details['car_model']}")
            print(f"Price Per Day : ₹{details['price_per_day']}")
            print(f"Rental Days : {details['rental_days']}")
            print(f"Total Bill : ₹{total_bill}")
            print("---------------------------")       
                
        else:
            print("\n This car is not currently rented:")
            
    else:
        print("\n Car not found")
        
        
def delete_car():
    car_id = input("Enter car Id:")
    
    if car_id in cars:
        del cars[car_id]
        
        print("\n Car Deleted Successfully!")
        print("--------------------------------")
        
    else:
        print("\n Car not found!")
        
def main_menu():
    
    while True:
        
        print("\n===== CAR RENTAL MANAGEMENT SYSTEM =====")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Search Car")
        print("4. Rent Car")
        print("5. Return Car")
        print("6. Calculate Rental Bill")
        print("7. Delete Car")
        print("8. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == "1":
            add_car()
        
        elif choice == "2":
            view_cars() 
            
        elif choice == "3":
            search_car()
            
        elif choice == "4":
            rent_car()
            
        elif choice == "5":
            return_car()
            
        elif choice == "6":
            calculate_bill()
            
        elif choice == "7":
            delete_car()
            
        elif choice == "8":
            print("Thank you for using CAR RENTAL MANAGEMENT SYSTEM!")
            
            break
        
        else:
            print("\n Invalid choice! Please try again!")
            
main_menu()
   
                