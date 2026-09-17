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
        print("\n Transaction Not Found!")
        return
    
    for trnasaction in transactions:
        
        print(f"Transaction Type : {transaction_type}")
        print("f Category : {category}")
        print("f Amount : {amount}") 
        print("---------------------------")
        
        
    
    