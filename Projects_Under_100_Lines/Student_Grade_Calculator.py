name = input("Enter student name: ")

math = int(input("Enter Math marks: "))
physics = int(input("Enter Physics marks: "))
english = int(input("Enter English marks: "))
chemistry = int(input("Enter Chemistry marks: "))
urdu = int(input("Enter Urdu marks: "))

total = math + physics + english + chemistry + urdu  
average = total / 5

if average >= 90:
    grade = "A+"

elif average >= 80:
    grade = "A"

elif average >= 70:
    grade = "B"

elif average >= 60:
    grade = "C"

elif average >= 40:
    grade = "D"

else:
    grade = "Fail"

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)