# Menu of Restaurant

menu = {

    "Veg": {

        "veg biryani": 179,
        "paneer biryani": 199,
        "zeera rice": 149,
        "curd rice": 139,
        "steam rice": 109
    },

    "Non-Veg": {

        "chicken dum biryani": 220,
        "chicken 65 biryani": 239,
        "mutton biryani": 259,
        "egg biryani": 189,
        "chicken family biryani": 510
    },

    "Pulao": {

        "veg pulao": 179,
        "kaju pulao": 199,
        "paneer pulao": 189,
        "jeera pulao": 200,
        "rajugadi kodi pulao": 250
    }
}

print("Welcome to Python Restaurant\n")

# Print Menu

for category, items in menu.items():

    print(f"---------- {category} ----------")
    
    print()

    for item, price in items.items():
        print(f"{item:<30}: ₹{price}")

    print()


# Total Amount

Order_Total = 0

# First Order

item_1 = input("Enter the name of item that you want to order: ").lower().strip()

found = False

for category, items in menu.items():

    if item_1 in items:

        Order_Total += items[item_1]

        print(f"Your item '{item_1}' has been added to your order")

        found = True
        
        break

if not found:
    print(f"Ordered item '{item_1}' is not available")


# Second Order

another_order = input("Do you want to add another item? (Yes/No): ").lower().strip()

if another_order == "yes":

    item_2 = input("Enter the name of second item: ").lower().strip()

    found = False

    for category, items in menu.items():

        if item_2 in items:

            Order_Total += items[item_2]

            print(f"Your item '{item_2}' has been added to your order")

            found = True
            break

    if not found:
        print(f"Ordered item '{item_2}' is not available")


# Final Bill

print(f"\nThe total amount of your order is ₹{Order_Total}")