from data import inventory
from file_handler import save_inventory
from validation import (
    get_valid_price,
    get_valid_quantity
)

def update_product():
    print("\n----- Update Product -----")
    update_id = int(input("Enter Product ID to Update: "))
    for product in inventory:
        if product["id"] == update_id:
            print("\nProduct Found")
            # product["name"] = input("Enter New Product Name: ")
            new_name = input("Enter New Product Name: ").strip()
            if new_name != "":
                product["name"] = new_name
            product["price"] = get_valid_price() #float(input("Enter New Product Price: "))
            product["quantity"] = get_valid_quantity() #int(input("Enter New Product Quantity: "))
            save_inventory()
            print("\nProduct Updated Successfully.")
            return
    print("\nProduct Not Found.")