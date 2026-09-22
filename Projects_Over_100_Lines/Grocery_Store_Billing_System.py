
# Step 1: Store all grocery products with their ID, name and price
products = {
    1: {"name": "Rice", "price": 60},
    2: {"name": "Wheat", "price": 40},
    3: {"name": "Sugar", "price": 80},
    4: {"name": "Milk", "price": 30},
    5: {"name": "Bread", "price": 40},
    6: {"name": "Eggs", "price": 8},
    7: {"name": "Oil", "price": 120},
    8: {"name": "Biscuits", "price": 50}
}


# Step 2: Display the program title
print("\n===== GROCERY STORE BILLING SYSTEM =====")


# Step 3: Take the customer's name
customer_name = input("Enter Customer Name: ")


# Step 4: Create an empty list to store purchased products
cart = []


# Step 5: Keep the program running until the customer generates the bill or exits
while True:

    # Step 6: Display the product menu
    print("\n===== PRODUCT MENU =====")

    # Step 7: Display all products with their ID, name and price
    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} - ₹"
            f"{product['price']}"
        )

    # Step 8: Display bill and exit options
    print("9. Generate Bill")
    print("10. Exit")

    # Step 9: Take the customer's choice
    choice = input("\nEnter your Choice: ")


    # Step 10: Exit the program if customer chooses 10
    if choice == "10":
        print("\nThank you for visiting.")
        break


    # Step 11: Generate the bill if customer chooses 9
    elif choice == "9":

        # Step 12: Check whether the cart is empty
        if len(cart) == 0:
            print("\nCart is empty.")
            continue


        # Step 13: Display the bill heading
        print("\n===== BILL =====")
        print(f"Customer Name: {customer_name}")
        print("-" * 30)


        # Step 14: Start subtotal from zero
        subtotal = 0


        # Step 15: Go through every product present in the cart
        for item in cart:

            # Step 16: Calculate the total price of the current item
            item_total = item["price"] * item["quantity"]

            # Step 17: Display the product, quantity and item total
            print(
                f"{item['name']} x {item['quantity']} "
                f"= ₹{item_total}"
            )

            # Step 18: Add the current item total to the subtotal
            subtotal += item_total


        # Step 19: Display the subtotal
        print("-" * 30)
        print(f"Subtotal: ₹{subtotal}")


        # Step 20: Apply discount according to the subtotal
        if subtotal >= 1000:

            # 10% discount for purchases of ₹1000 or more
            discount = subtotal * 0.10
            print("Discount: 10%")

        elif subtotal >= 500:

            # 5% discount for purchases of ₹500 or more
            discount = subtotal * 0.05
            print("Discount: 5%")

        else:

            # No discount for purchases below ₹500
            discount = 0
            print("Discount: 0%")


        # Step 21: Calculate the final amount after discount
        final_amount = subtotal - discount


        # Step 22: Display discount amount and final amount
        print(f"Discount Amount: ₹{discount:.2f}")
        print(f"Final Amount: ₹{final_amount:.2f}")


        # Step 23: Display the final thank-you message
        print("-" * 30)
        print("Thank you for shopping!")


        # Step 24: End the program after generating the bill
        break


    # Step 25: Check whether the customer selected a valid product
    elif choice.isdigit() and 1 <= int(choice) <= 8:

        # Step 26: Convert the selected product ID from string to integer
        product_id = int(choice)


        # Step 27: Get the selected product from the products dictionary
        selected_product = products[product_id]


        # Step 28: Display the selected product details
        print(f"\nSelected Product: {selected_product['name']}")
        print(f"Price: ₹{selected_product['price']}")


        # Step 29: Ask the customer for the quantity
        quantity = input("Enter Quantity: ")


        # Step 30: Validate the quantity
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid Quantity!")
            continue


        # Step 31: Convert quantity from string to integer
        quantity = int(quantity)


        # Step 32: Create a dictionary for the purchased item
        item = {
            "name": selected_product["name"],
            "price": selected_product["price"],
            "quantity": quantity
        }


        # Step 33: Add the purchased item to the cart
        cart.append(item)


        # Step 34: Calculate the total price of the current item
        total = selected_product["price"] * quantity


        # Step 35: Show confirmation to the customer
        print(f"{selected_product['name']} Added to cart.")
        print(f"Item Total: ₹{total}")


    # Step 36: Handle invalid menu choices
    else:
        print("Invalid Choice! Please try again.")
