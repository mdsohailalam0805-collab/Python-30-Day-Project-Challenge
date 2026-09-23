
# Simple Shopping Bill Calculator
name = input("enter your name:")

item1 = int(input("enter price of item1:"))
item2 = int(input("enter price of item2:"))
item3 = int(input("enter price of item3:"))
item4 = int(input("enter price of item4:"))

total = item1 + item2 + item3 + item4

if total > 2000:
    discount = total * 0.10
else:
    discount = 0
    
    
final_amount = total - discount

print("\n----SHOPPING BILL")
print("Customer name" , name)
print("Total amount" , total)
print("Discount" , discount)
print("Final_amount" , final_amount)