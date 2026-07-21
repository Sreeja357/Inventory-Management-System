from data import inventory
from file_handler import save_inventory

def stock_in():
    print("\n----- Stock In -----")
    stock_id = int(input("Enter Product ID: "))
    for product in inventory:
        if product["id"] == stock_id:
            # add_quantity = int(input("Enter Quantity to Add: "))
            while True:
                try:
                    add_quantity = int(input("Enter Quantity to Add: "))
                    if add_quantity > 0:
                        break
                    print("Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid Quantity.")

            product["quantity"] += add_quantity
            save_inventory()
            print("\nStock Updated Successfully.")
            print("Current Quantity:", product["quantity"])
            return
    print("\nProduct Not Found.")