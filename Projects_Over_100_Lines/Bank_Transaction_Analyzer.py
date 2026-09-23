transactions = []

def add_transaction():
    
    transaction_type = input("Enter transaction type (Income/Expense):")
    category = input("Enter Category:")
    amount = float(input("Enter amount:"))
    
    transaction = {
        "type" : transaction_type,
        "category" : category,
        "amount" : amount
    }
    
    transactions.append(transaction)
    
    print("\n Transaction Added Successfully!")
    
    print(f"Type : {transaction_type}")
    print(f"Category : {category}")
    print(f"Amount : {amount:.2f}")
    print("-----------------------------")
    
    
def view_transactions():
    
    if not transactions:
        print("\nNo Transaction Available!")
        return
    
    print("\n===== ALL TRANSACTIONS =====")
        
    for transaction in transactions:
        
        print(f"Transaction Type : {transaction['type']}")
        print(f"Category : {transaction['category']}")
        print(f"Amount : ₹{transaction['amount']:.2f}")
        print("---------------------------")
        
        
def calculate_balance():
    
    total_income = 0
    total_expense = 0
    
    for transaction in transactions:
        
        if transaction["type"].lower() == "income":
            total_income += transaction["amount"] 
            
        elif transaction["type"].lower() == "expense":
            total_expense += transaction["amount"]
            
        balance = total_income - total_expense
        
        print("\n BALANCE SUMMARY!")
        print(f"Total Income : {total_income:.2f}")
        print(f"Total Expense : {total_expense:.2f}")
        print(f"Current Balance : {balance:.2f}")
        print("---------------------------------------")
    

def highest_expense():
    highest = None
    
    for transaction in transactions:
        
        if transaction["type"].lower() == "expense":
            
            if highest is None or transaction["type"] > highest["amount"]:
                highest = transaction
                
    if highest is None:
        print("\n No expense Transaction Available!")
        return
    
    print("\n =====HIGHEST EXPENSE=====")
    
    print(f"Category : {highest['category']}")
    print(f"Amount : {highest['amount']}")
    print("-----------------------------") 
    
    
def transaction_summary():
    
    total_income = 0
    total_expense = 0
    income_count = 0
    expense_count = 0
    
    for transaction in transactions:
        
        if transaction["type"].lower() == "income":
            total_income += transaction["amount"]
            income_count += 1
            
        elif transaction["type"].lower() == "expense":
            total_expense += transaction["amount"]
            expense_count += 1
        
    balance = total_income - total_expense
            
    print("\n =====TRANSACTION SUMMARY=====")
    print(f"Total Income : {total_income:.2f}")
    print(f"Income Transaction : {income_count:.2f}")
    print(f"Total Expense : {total_expense:.2f}")
    print(f"Expense Transaction : {expense_count:.2f}")
    print(f"Current Balance : {balance:.2f}")
    print("-------------------------------")
    
    
def main_menu():

    while True:

        print("\n===== BANK TRANSACTION ANALYZER =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Balance")
        print("4. Find Highest Expense")
        print("5. Transaction Summary")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            calculate_balance()

        elif choice == "4":
            highest_expense()

        elif choice == "5":
            transaction_summary()

        elif choice == "6":
            print("\nThank You For Using Bank Transaction Analyzer!")
            break

        else:
            print("\nInvalid Choice! Please Try Again!")


main_menu()