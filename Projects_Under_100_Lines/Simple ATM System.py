
name = input("enter your name:")

Balance = 3000
print("\n-- Welcome--", name)
print("Your balance is ", Balance)

print("1. Deposit")
print("2. Withdraw")

choice = int(input("enter your choice:"))

if choice == 1:
    amount = int(input("enter deposit amount:"))
    Balance = Balance + amount
    print("Amount Deposited successfully")
    
elif choice == 2:
    amount= int(input("enter withdraw amount:"))
    
    if amount <= Balance:
        Balance = Balance - amount
        print("withdrawl successfully")
        
    else:
        print("insuffficient Balance")

else:
    print("Invalid choice")
    
print("\n*****ATM SUMMARY*****")
print("Account Holder :", name)
print("Final Balance :", Balance)
          
    
