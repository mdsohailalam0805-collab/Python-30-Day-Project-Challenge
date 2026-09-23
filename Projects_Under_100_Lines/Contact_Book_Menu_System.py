contacts = {}

def add_contacts():
    name = input("Enter contact name:")
    phone = input("Enter phone number:")
    
    contacts[name] = phone 
    
    print("Added contact Successfully!")


def search_contacts():
    name = input("Enter the name you want to Search:")
    
    if name in contacts:
        print("Name:", name)
        print("phone:", contacts[name])    
        
    else:
        print("contact not found")
        
def delete_contacts():
    name = input("Enter the name you want to delete:")
    
    if name in contacts:
        del contacts[name]
        print("Contact Deleted Successfully.")
        
    else:
        print("Contact not found.")
        
def view_contacts():
    
    if len(contacts) == 0:
        print("No Contacts Available.")
        
    else:
        print("***** All Contacts *****")
        
        for name, phone in contacts.items():
            print(name, ":", phone)

while True:
    
    print("\n===== Contacts Book =====")
    
    print("1. Add contacts")
    print("2. Search contacts")
    print("3. Delete contacts")
    print("4. View All contacts")
    print("5. Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        add_contacts()
        
    elif choice == "2":
        search_contacts()
        
    elif choice == "3":
        delete_contacts()
        
    elif choice == "4":
        view_contacts()
        
    elif choice == "5":
        print("Thank you for using contact Book.")
        break
        
    else:
        print("Invalid choice! Please try Again.")
          