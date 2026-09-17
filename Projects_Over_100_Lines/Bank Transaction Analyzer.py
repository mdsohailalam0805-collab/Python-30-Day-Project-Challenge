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
    
    
def view_transaction():
    
    if not transaction:
        print("\n No Transaction Available!")
        return
    
        print("\n All Transaction.")
        
    for trnasaction in transactions:
        
        print(f"Transaction Type : {transaction['transaction_type']}")
        print("f Category : {transaction['category']}")
        print("f Amount : {transaction['amount']:.2f}") 
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
    
    