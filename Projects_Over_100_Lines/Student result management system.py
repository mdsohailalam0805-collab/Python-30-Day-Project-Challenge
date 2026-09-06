# Student data store karne ke liye empty list
students = []


# Marks ke average ke according grade calculate karta hai
def calculate_grade(marks):
    # Marks ka average calculate karna
    average = sum(marks) / len(marks)

    # Grade decide karna
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# New student add karne ka function
def add_student():
    print("\n--- Add Student ---")

    # Student ki basic information lena
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    # Marks store karne ke liye empty list
    marks = []

    # Subjects ki list
    subjects = ["Python", "Maths", "English", "Science", "Computer"]

    # Har subject ke marks lena
    for subject in subjects:
        while True:
            try:
                # User se marks input lena
                mark = float(input(f"Enter {subject} marks: "))

                # Marks ko validate karna
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            # Invalid input handle karna
            except ValueError:
                print("Please enter a valid number.")

    # Student ki information dictionary me store karna
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    # Student ko main list me add karna
    students.append(student)

    print("\nStudent added successfully!")


# Sabhi students ko display karne ka function
def view_students():
    print("\n--- All Students ---")

    # Agar student list empty hai
    if not students:
        print("No students found.")
        return

    # Har student ki information display karna
    for student in students:
        # Average calculate karna
        average = sum(student["marks"]) / len(student["marks"])

        # Grade calculate karna
        grade = calculate_grade(student["marks"])

        print(f"\nRoll Number : {student['roll']}")
        print(f"Name        : {student['name']}")
        print(f"Marks       : {student['marks']}")
        print(f"Average     : {average:.2f}")
        print(f"Grade       : {grade}")


# Roll number ke through student search karna
def search_student():
    print("\n--- Search Student ---")

    # Roll number input lena
    roll = input("Enter Roll Number: ")

    # Students list me search karna
    for student in students:
        # Roll number match karna
        if student["roll"] == roll:
            # Average calculate karna
            average = sum(student["marks"]) / len(student["marks"])

            print("\nStudent Found!")
            print("Name    :", student["name"])
            print("Marks   :", student["marks"])
            print("Average :", round(average, 2))
            print("Grade   :", calculate_grade(student["marks"]))

            # Student mil gaya, loop stop
            return

    # Agar student nahi mila
    print("Student not found.")


# Class ka topper find karna
def find_topper():
    print("\n--- Class Topper ---")

    # Agar student list empty hai
    if not students:
        print("No students available.")
        return

    # Starting me first student ko topper maan lena
    topper = students[0]

    # Sabhi students ko check karna
    for student in students:
        # Current student ke marks topper se compare karna
        if sum(student["marks"]) > sum(topper["marks"]):
            # Agar marks zyada hain to topper update karna
            topper = student

    # Topper ka average calculate karna
    average = sum(topper["marks"]) / len(topper["marks"])

    print("Topper Name :", topper["name"])
    print("Roll Number :", topper["roll"])
    print("Average     :", round(average, 2))
    print("Grade       :", calculate_grade(topper["marks"]))


# Puri class ka average calculate karna
def class_average():
    print("\n--- Class Average ---")

    # Agar student list empty hai
    if not students:
        print("No students available.")
        return

    # Total marks aur total subjects count karna
    total = 0
    count = 0

    # Har student ke marks process karna
    for student in students:
        # Student ke total marks add karna
        total += sum(student["marks"])

        # Subjects ki count add karna
        count += len(student["marks"])

    # Class average calculate karna
    average = total / count

    print("Class Average:", round(average, 2))


# Roll number ke through student delete karna
def delete_student():
    print("\n--- Delete Student ---")

    # Roll number input lena
    roll = input("Enter Roll Number: ")

    # Student search karna
    for student in students:
        # Roll number match karna
        if student["roll"] == roll:
            # Student ko list se remove karna
            students.remove(student)

            print("Student deleted successfully.")

            # Delete hone ke baad function stop
            return

    # Student nahi mila
    print("Student not found.")


# Program ka main function
def main():
    # Program ko continuously run karna
    while True:
        # Menu display karna
        print("\n****************************")
        print("   STUDENT RESULT SYSTEM")
        print("****************************")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Class Average")
        print("6. Delete Student")
        print("7. Exit")
        print("****************************")

        # User se menu choice lena
        choice = input("Enter your choice: ")

        # Add student
        if choice == "1":
            add_student()

        # View students
        elif choice == "2":
            view_students()

        # Search student
        elif choice == "3":
            search_student()

        # Find topper
        elif choice == "4":
            find_topper()

        # Calculate class average
        elif choice == "5":
            class_average()

        # Delete student
        elif choice == "6":
            delete_student()

        # Exit program
        elif choice == "7":
            print("Thank you for using Student Result System!")
            break

        # Invalid choice handle karna
        else:
            print("Invalid choice. Try again.")


# Main function ko call karke program start karna
main()