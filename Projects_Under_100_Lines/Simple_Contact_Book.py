contacts = {} # Dictionary to store contacts

print("Welcome to contact book!")

name = input("Enter your name:")
phone = input("Enter your phone number:")

contacts[name] = phone

print("Contact added successfully!")

print("------------------------------------------------------)")
choice = input("Do you want to add another contact? (yes/no):")

while choice.lower() == "yes":
    name = input("Enter your name:")
    phone = input("Enter your phone number:")
    
    contacts[name] = phone
    
    print("Contact added successfully!")
    print("--------------------------------")
    
    choice = input("Do you want to add another contact? (yes/no):")

print("---------------------------------------------------------")    
choice = input("Do you want to search for a contact? (yes/no):")

if choice.lower() == "yes":
    search_name = input("Enter the name of the contact you want to search for:")
    
    if search_name in contacts:
        print("Name", search_name)
        print("Phone", contacts[search_name])
        
    else:
        print("Contact not found")
        
print("---------------------------------------------------")       
choice = input("Do you want to delete a contact? (yes/no):")

if choice.lower() == "yes":
    delete_name = input("Enter the name of the contact you want to delete:")
    
    if delete_name in contacts:
        del contacts[delete_name]
        print("Contact deleted Succesfully")
        
    else:
        print("Contact not found")

print("\n All contacts")

for name, phone in contacts.items():
    print(name, ":", phone)

print("\n Total Contacts:", len(contacts))
print("Thank you for using contact Book")    


    