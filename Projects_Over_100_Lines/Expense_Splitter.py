people = []

def add_person():
    name = input("Enter person name:")
    
    people.append(name)
    
    print("\n Person Added Successfully!")
    print(f"Name : {name}")
    print("-------------------------------")
    
expenses = {}

def add_expenses():
    name = input("Enter person Name:")
    
    if name not in people:
        print("\n Person Not Found!") 
        return
    
    amount = float(input("Enter expense amount:"))
    
    expenses[name] = amount
    
    print("\n Expense Added Successfully!")
    print(f"Name : {name}")
    print(f"Amount : {amount}")
    print("-------------------------------")
    
def view_expenses():
        if not expenses:
            print("\n No Expenses Available!")
            return
        
        print("\n=====ALL EXPENSES=====")
        
        for name, amount in expenses.items():
            print(f"Person : {name}")
            print(f"Amount : {amount}")
            print("---------------------------")
            
            
def calculate_split():
    if not people:
        print("\n No people Available!")
        return
    
    total_expense = sum(expenses.values())
    per_person_share = total_expense / len(people)
    
    print("\n =====EXPENSE SPLIT=====")
    print(f"Total Expense : {total_expense}")
    print(f"Total People : {len(people)}")
    print(f"Per Person Share : {per_person_share}")
    print("----------------------------------------")
    
    
def view_settlement():
    
    if not people:
        print("\n No People Available!")
        return
    
    total_expense = sum(expenses.values())
    per_person_share = total_expense / len(people)
    
    print("\n =====SETTELEMENT=====")
    
    for name in people:
        
        paid_amount = expenses.get(name, 0) 
        difference = paid_amount - per_person_share
        
        if difference > 0:
            print(f"{name} should receive {difference:.2f}")       
            
        elif difference < 0:
            print(f"{name} should pay {abs(difference):.2f}")
            
        else:
            print(f"{name} is settled.")
            
    print("------------------------------------------")
    
def main_menu():

    while True:

        print("\n===== EXPENSE SPLITTER =====")
        print("1. Add Person")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Calculate Split")
        print("5. View Settlement")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_person()

        elif choice == "2":
            add_expenses()

        elif choice == "3":
            view_expenses()

        elif choice == "4":
            calculate_split()

        elif choice == "5":
            view_settlement()

        elif choice == "6":
            print("\nThank You For Using Expense Splitter!")
            break

        else:
            print("\nInvalid Choice! Please Try Again!")


main_menu()