# 🛒 Inventory Management System

inventory = {}


# 1️ Add Product
def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))

    inventory[product_name] = {
        "price": price,
        "stock": stock
    }

    print("\nProduct added successfully!")


# 2️ View All Products
def view_products():
    if not inventory:
        print("\nInventory is empty!")
        return

    print("\n--- All Products ---")

    for product_name, details in inventory.items():
        print(f"Product: {product_name}")
        print(f"Price: ₹{details['price']}")
        print(f"Stock: {details['stock']}")
        print("--------------------")


# 3️ Search Product
def search_product():
    product_name = input("Enter product name to search: ")

    if product_name in inventory:
        details = inventory[product_name]

        print("\nProduct found!")
        print(f"Product: {product_name}")
        print(f"Price: ₹{details['price']}")
        print(f"Stock: {details['stock']}")
    else:
        print("\nProduct not found!")


# 4️ Update Stock
def update_stock():
    product_name = input("Enter product name: ")

    if product_name in inventory:
        new_stock = int(input("Enter new stock: "))

        inventory[product_name]["stock"] = new_stock

        print("\nStock updated successfully!")
        print(f"Product: {product_name}")
        print(f"New Stock: {inventory[product_name]['stock']}")
    else:
        print("\nProduct not found!")


# 5️ Delete Product
def delete_product():
    product_name = input("Enter product name to delete: ")

    if product_name in inventory:
        del inventory[product_name]

        print("\nProduct deleted successfully!")
    else:
        print("\nProduct not found!")


# 6️ Total Inventory Value
def total_inventory_value():
    total_value = 0

    for product_name, details in inventory.items():
        product_value = details["price"] * details["stock"]
        total_value += product_value

    print(f"\nTotal Inventory Value: ₹{total_value}")


# # Function Calls
# add_product()
# add_product()

# view_products()

# search_product()

# update_stock()

# delete_product()

# total_inventory_value()

# 7️ Main Menu

def main_menu():
    
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Total Inventory Value")
        print("7. Exit")

        choice = input("Enter your choice:")
        
        if choice == "1":
            add_product()
        
        elif choice == "2":
            view_products()
            
        elif choice == "3":
            search_product()
            
        elif choice == "4":
            update_stock()
            
        elif choice == "5":
            delete_product()
            
        elif choice == "6":
            total_inventory_value()
            
        elif choice == "7":
            print("\n Thank you for using Inventory management system.")
            
            break 
            
        else:
            print("Invalid choice ! Please try Again.")
            
# start program
main_menu()
            
        