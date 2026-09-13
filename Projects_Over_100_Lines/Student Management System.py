
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
    
add_student()
print(students)

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
        
view_student()


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
        
        
search_student()