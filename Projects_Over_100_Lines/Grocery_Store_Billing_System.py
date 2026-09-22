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
        print(f"{product_id}. {product['name']} - ₹"
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
        
    # Product selection check
    
    elif choice.isdigit() and 1 <= int(choice) <= 8:
        product_id = int(choice)
        
        selected_product = products[product_id]
        print(f"\n Selected Product : {selected_product['name']}")
        print(f"Price : {selected_product['price']}")
        
        quantity = input("Enter Quantity:")
        
        if not quantity.isdigit() or int(quantity) <=0:
            print("Invalid Quantity")
            continue
        
        quantity = int(quantity)
        
    item = {
        "name" : selected_product["name"],
        "price" : selected_product["price"],
        "quantity": quantity
}

    cart.append(item)
    
    total = selected_product["price"] * quantity
    
    print(f"{selected_product['name']} Added to cart.")
    print(f"Item Total : {total}")
    
    print("\n=====BILL=====")
    print(f"Customer Name : {customer_name}")
    print("-" * 30)
    
    
    subtotal = 0
    
    for item in cart:
        
        item_total = item['price'] * item['quantity']
        print(f"{item['name']} x {item['quantity']} = ₹{item_total}")
        
        subtotal += item_total
    print("-" * 30)
    print(f"Subtotal : {subtotal}")
    
    
    # : Discount condition
    
    if subtotal >= 1000:
        discount = subtotal * 0.10
        print("Discount : 10%")
        
    elif subtotal >= 500:
        discount = subtotal * 0.05
        print("Discount : 5%")

    else:
        discount = 0
        print("Discount : 0%")