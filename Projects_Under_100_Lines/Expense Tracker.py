# Expenses Tracker

expense = {}

def add_expenses():
    
    item = input("Enter Expense Name:")
    amount = float(input("Enter Expense Amount:"))
    
    expense[item] = amount
    
    print("Expense added Successfully.")
    
def view_expense():
    
    if len(expense) == 0:
        print("No Expenses is Available")
            
    else:
        print("\n ----- All Expenses -----")
            
        for item , amount in expense.items():
            print(item, ":", amount)
                
def total_expense():
    
    if len(expense) == 0:
        print("No Expenses is Available.")
        
    else:
        total = sum(expense.values())
        print("Total Expense", total)
        
while True:
    print("\n----- Expense Tracker -----")
    
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    
    choice = input("Enter your Choice:")
    
    if choice == "1":
        add_expenses()
        
    elif choice == "2":
        view_expense()
        
    elif choice == "3":
        total_expense()
        
    elif choice == "4":
        
        print("Thank You For Using Expense Tracker.")
        
        break
    
    else:
        print("Invalid Choice! Please Try Again.")