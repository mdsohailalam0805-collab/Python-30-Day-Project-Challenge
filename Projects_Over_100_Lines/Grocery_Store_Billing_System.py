products = {
    1: {"name" : "Rice", "price" : 60},
    2: {"name" : "Wheat", "price" : 40},
    3: {"name" : "Sugar", "price" : 80},
    4: {"name" : "Milk", "price" : 30},
    5: {"name" : "Bread", "price" : 40},
    6: {"name" : "Eggs", "price" : 8},
    7: {"name" : "Oil", "price" : 120},
    8: {"name" : "Biscuits", "price" : 50}
}

print("\n =====GROCERY STORE BILLING SYSTEM=====")

customer_name = input("Enter Customer Name:")

cart = []

while True:
    
    print("\n=====PRODUCT MENU=====")
    
    for product_id,product in products.items():
        print(f"product_id : {product['name']} -"
              f"{product['price']}")
        
    print("9. Generate Bill")
    print("10. Exit")
    
    choice = input("\nEnter your Choice:")
    
    if choice == "10":
        print("\n Thank you for visiting.")
        break
    
    elif choice == "9":
        
        if len(cart) == 0:
            print("\n cart is empty.")
            continue
        
        