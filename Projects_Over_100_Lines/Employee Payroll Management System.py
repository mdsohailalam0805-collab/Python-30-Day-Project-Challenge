employees = {}

def add_employee():
    
    employee_name = input("Enter employee name you want to add:")
    salary = float(input("Enter monthly salary:"))
    working_days = int(input("Enter working days:"))
    
    employees[employee_name] = {
        "salary" : salary,
        "working_days" : working_days
    }
    
    print("\n Employee Added Successfully.")
    
    print("------------------------------------")
    

def view_employee():
    
    if not employees:
        print("\n Employee not found.")
        return
    print("---------------------")
    
    print("\n All Employees.")
    
    for employee_name, details in employees.items():
        print(f"Employee name: {employee_name}")
        print(f"Monthly Salary: {details['salary']}")
        print(f"Working days: {details['working_days']}")
        print("------------------------------------------")  
        

def calculate_salary():
    
    employee_name = input("Enter the employee name whose salary want to calculate:")
    
    if employee_name in employees:
        details = employees[employee_name]
        
        monthly_salary = details['salary']  
        working_days = details['working_days']  
        
        daily_salary = monthly_salary / 26
        net_salary = daily_salary * working_days
        
        print("\n Salary Details.")
        
        print(f"Employee name : {employee_name}")
        print(f"Monthly salary : {monthly_salary}")
        print(f"Working Days : {working_days}")
        print(f"Daily Salary : {daily_salary:.2f}")
        print(f"Net Salary : {net_salary:.2f}")
        
    else:
        print("\n Employee not found.")
        print("---------------------------")
        
def update_salary():
    employee_name = input("Enter Employee name whose salary want to upadate:")
    
    if employee_name in employees:
        new_salary = float(input("Enter New Monthly Salary:"))
        
        employees[employee_name]['salary'] = new_salary
        print("\n Salary Updated Successfully:")
        
    else:
        print("\nEmployee not found! ") 
        
        
def delete_employee():
    employee_name = input("Enter the Employee name whose you want to delete:")
    
    if employee_name in employees:
        del employees[employee_name]
        print("\n Employee Deleted Successfully!") 
        
    else:
        print("Employee not Found!")
        
                
while True:
    print("===== EMPLOYEE PAYROLL MANAGEMENT SYSTEM =====")
    
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Calacualate Salary")
    print("4. Update Salary")
    print("5. Delete employee")
    print("6. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        add_employee()
        
    elif choice == "2":
        view_employee()
        
    elif choice == "3":
        calculate_salary()
        
    elif choice == "4":
        update_salary()
        
    elif choice == "5":
        delete_employee()
        
    elif choice == "6":
        
        print("Thank You For Using Employee Payroll Management.")
        break
    
    else:
        print("Invalid Choice, Please Try Again!")
    