
students = {}

def add_student():
    student_id = input("Enter Student ID:")
    student_name = input("Enter Student Name:")
    age = input("Enter Student Age:")
    course = input("Enter Course:")
    
    students[student_id] = {
        "student_name" : student_name,
        "age" : age,
        "course" : course
    }
    
    print("\n Student Added Successfully!")
    print("---------------------------------")
    

def view_student():
    
    if not students:
        print("\n Student Not Available!")
        return
    
    for student_id, details in students.items():
        print("------STUDENT DETAILS------")
        
        print(f"Student ID : {student_id}")
        print(f"Student Name : {details['student_name']}")
        print(f"Age : {details['age']}")
        print(f"Course : {details['course']}")
        print("-----------------------------------")


def search_student():
    student_id = input("Enter Student ID:")
    
    if student_id in students:
        details = students[student_id]
        
        print("------STUDENT DETAILS------")
        print(f"Student ID : {student_id}")
        print(f"Student Name : {details['student_name']}")
        print(f"Age : {details['age']}")
        print(f"Course : {details['course']}")
        print("---------------------------------")
        
        
    else:
        print("\n Student Not Available!")
        print("----------------------------")
        

def update_student():
    student_id = input("Enter Student ID:")
    
    if student_id in students:
        details = students[student_id]
        
        new_name = input("Enter new student name:")
        new_age = input("Enter new student Age:")
        new_course = input("Enter new course name:")
        
        details["name"] = new_name
        details["age"] = new_age
        details["course"] = new_course
        
        print("\n Student update successfully!")
        print("-----------------------------------")
        
    else:
        print("\n Student not found!")
        print("-------------------------------")
        

def calculate_result():
    student_id = input("Enter Student ID:")
    
    if student_id not in students:
        print("\nEnter not found!")
        return
    
    print("\n Enter marks for 5 subjects.")
    
    subject1 = float(input("subject 1:"))
    subject2 = float(input("subject 2:"))
    subject3 = float(input("subject 3:"))
    subject4 = float(input("subject 4:"))
    subject5 = float(input("subject 5:"))
    
    total = subject1 + subject2 + subject3 + subject4 + subject5
    
    percentage = total/5
    
    if percentage >=90:
        grade = "A+"
        
    elif percentage >=80:
        grade = "A"
        
    elif percentage >=70:
        grade = "B"
        
    elif percentage >=60:
        grade = "C"
        
    elif percentage >=50:
        grade = "D"
        
    else:
        grade = "F"
    
    print("\n===== STUDENT RESULT =====")  
    print(f"Student ID: {student_id}")
    print(f"Student Name: {students[student_id]['student_name']}")
    print(f"Total Marks : {total}")
    print(f"percentage : {percentage:.2f}%")
    print(f"Grade : {grade}")
    print("--------------------------------")
    


def delete_student():
    student_id = input("Enter Student ID:")
    
    if student_id in students:
        del students[student_id]
        
        print("\n Student Deleted Successfully!")
        print("------------------------------------")
        
    else:
        print("\nStudent not found!")
        print("------------------------")
        
def main_menu():
    
    while True:
        
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Calculate Result")
        print("6. Delete Student")
        print("7. Exit")
        
        choice = input("Enter your Choice:")
        
        if choice =="1":
            add_student()
            
        elif choice =="2":
            view_student()
            
        elif choice == "3":
            search_student()
            
        elif choice == "4":
            update_student()
            
        elif choice == "5":
            calculate_result()
            
        elif choice == "6":
            delete_student()
            
        elif choice == "7":
            print("Thank You For Using This Application.")
            break
        
        else:
            print("Invalid Choice, Try Again!")
            break
        
main_menu()