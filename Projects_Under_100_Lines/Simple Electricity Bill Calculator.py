# Simple Electricity Bill Calculator

name = input("enter your name :")

units = int(input("enter your electricity units :"))

if units <=200:
    bill = units * 5
    
elif units <=300:
    bill = 300 * 7
    
else:
    bill = units*10
    
print("\n***** Electricity Bill *****")
print("------------------------------")
print("User Name :", name)
print("Units used :", units)
print("Total Bill :" , bill)  
    
    
