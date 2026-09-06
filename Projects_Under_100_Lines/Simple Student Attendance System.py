students = ["Sohail", "Altamsh", "Waseem", "Sonu", "Shivam", "Suraj", "Rohit", "Harsh", "Azad", "Farhan", "Munawar"]

attendence ={}

print("\nWelcome to attendance system") 
print("--------------------------------\n")

for student in students:
    status = input(f"Is {student} present? (y/n): ").lower().strip()
    
    if status.lower() == "y": 
        attendence[student] = "present"
        
    elif status.lower() == "n":
        attendence[student] = "absent"
        
    else:
        attendence[student] = "No Marked"
        print('Invalid input, please enter "y" for present and "n" for absent.')    
        
print("\n ******Attendence Report******")

present = 0
absent = 0
No_Marked = 0

for student, status in attendence.items():
    print(f"{student}: {status}")
    
    if status.lower() == "present":
        present += 1
        
    elif status.lower() == "absent":
        absent += 1
           
    else:
        No_Marked += 1  

print(f"\n Total Students: {len(students)}")
print(f" Total Present: {present}")
print(f" Total Absent: {absent}")
print(f" Total No Marked: {No_Marked}")


print("\n ****** Thank you for using the attendence system ******")


