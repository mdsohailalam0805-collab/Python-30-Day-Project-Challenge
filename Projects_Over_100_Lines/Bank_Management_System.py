account = {}

def create_account():

    account_number = input("Enter Account number:")
    account_holder_name = input("Enter the account holder name:")
    initial_balance = float(input("Enter initial balance:"))
    
    account[account_number] = {
        "account_holder_name":account_holder_name,
        "initial_balance": initial_balance
    }
    
    print("\nAccount Created Successfully!")
    print("--------------------------------")
    
def view_account():
    
    account_number = input("Enter account number:")
    
    if account_number in account:
        details = account[account_number]
        
        print("========ACCOUNT DETAILS========")
        print(f"Account Number : {account_number}")
        print(f"Account Holder Name : {details['account_holder_name']}")
        print(f"initial balance : {details['initial_balance']}")
        
    else:
        print("\n Account not found!")
        print("------------------------------")
        
def deposit_money():
    account_number = input("Enter Account Number:")
    
    if account_number in account:
        amount = float(input("Enter the deposit ammount:"))
        
        if amount > 0:
            account[account_number]['initial_balance'] += amount
            
            print("\nMoney deposit successfully!")
            print(f"updated Balance : {account[account_number]['initial_balance']}")
            
        else:
            print("Deposit Amount must be greater than 0.")
            
    else:
        print("\n Account not found!")
        print("----------------------------------")
        
def withdraw_money():
    account_number = input("Enter Account number:")
    
    if account_number in account:
        withdraw_amount = float(input("Enter withdraw amount:"))
            
        if withdraw_amount <= 0:
           print("\n Withdraw amount must be greater than 0!")
            
        elif account[account_number]['initial_balance'] < withdraw_amount:
            print("\n Insufficient Balance!") 
            
        else:
            account[account_number]['initial_balance'] -= withdraw_amount
            print("\n Money withdraw Successfully!")
            print("-----------------------------------")
                            
    else:
        print('Account not found!')
        print("----------------------------------------")
        
def check_balance():
    account_number = input("Enter account number:")
    
    if account_number in account:
        print("===== BALANCE DETAILS =====") 
        print(f" Account Number : {account_number}")
        print(f"Account holder name : {account[account_number]['account_holder_name']}")  
        print(f"Initialy Balance : {account[account_number]['initial_balance']}")
        print("-----------------------------------------")
    else:
        print("\n Account not found!")
        print("------------------------------------------")
        
def delete_account():
    account_number = input("Enter account number:")
     
    if account_number in account:
        del account[account_number]
        print("\n Account deleted Successfully!")  
        print("-----------------------------------")
    else:
        print("\n Account not found!")              
        
def main_menu():
    
    while True:

        print("1. Create Account:")
        print("2. View Account:")
        print("3. Deposit Amount:")
        print("4. Withdraw Amount:")
        print("5. Check Balance:")
        print("6. Delete Account:")
        print("7. Exit")
    
        choice = input("Enter your choice:")
    
        if choice == "1":
            create_account()
        
        elif choice == "2":
            view_account()
        
        elif choice == "3":
            deposit_money()
        
        elif choice == "4":
            withdraw_money()
        
        elif choice == "5":
            check_balance()
        
        elif choice == "6":
            delete_account()
        
        elif choice == "7":
            print("\n Thank You For Using BANK_MANAGEMENT_SYSTEM!")
            break
    
        else:
            print("\n Invalid choice! Please try again.")
            
main_menu()
        