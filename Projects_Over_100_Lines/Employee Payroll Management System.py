employees = {}

def add_employee():
    
    employee_name = input("Enter employee name:")
    salary = float(input("Enter monthly salary:"))
    working_days = int(input("enter working days:"))
    
    employees[employee_name] = {
        "salary" : salary,
        "working_days" : working_days
    }
    
    print("\n Employee Added Successfully.")
    
    print("------------------------------------")
    

def view_employee():
    
    if not employee:
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
    
    employee_name = input("Enter employee name:")
    
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
    employee_name = input("Enter Employee name:")
    
    if employee_name in employees:
        new_salary = float(input("Enter New Monthly Salary:"))
        
        employees[employee_name]['salary'] = new_salary
        print("\n Salary Updated Successfully:")
        
    else:
        print("\nEmployee not found! ") 
        
        
def delete_employee():
    employee_name = input("Enter the Employee name you want to delete:")
    
    if employee_name in employees:
        del employees[employee_name]
        print("\n Employee Deleted Successfully!") 
        
    else:
        print("Employee not Found!")
        
        

    