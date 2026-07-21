from data import inventory
from file_handler import save_inventory

def stock_out():
    print("\n----- Stock Out -----")
    stock_id = int(input("Enter Product ID: "))
    for product in inventory:
        if product["id"] == stock_id:
            # sell_quantity = int(input("Enter Quantity Sold: "))
            while True:
                try:
                    sell_quantity = int(input("Enter Quantity sold: "))
                    if sell_quantity > 0:
                        break
                    print("Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid Quantity.")

            if sell_quantity <= product["quantity"]:
                product["quantity"] -= sell_quantity
                save_inventory()
                print("\nStock Updated Successfully.")
                print("Remaining Quantity:", product["quantity"])
            else:
                print("\nInsufficient Stock!")
            return
    print("\nProduct Not Found.")