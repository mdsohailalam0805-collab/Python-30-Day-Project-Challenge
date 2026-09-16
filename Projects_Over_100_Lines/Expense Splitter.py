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
    print(f"amount : {amount}")
    print("-------------------------------")
    
def view_expenses():
          