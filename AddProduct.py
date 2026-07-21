from data import inventory
from file_handler import save_inventory
from validation import (
    get_valid_price,
    get_valid_quantity
)

def add_product():
    print("\n----- Add Product -----")
    #  Manual Product ID Entry
    # product_id = int(input("Enter Product ID: "))
    # Check for duplicate Product ID
    # for product in inventory:
    #     if product["id"] == product_id:
    #         print("Product ID already exists!")
    #         return

    #  Automatic Product ID Generation
    if len(inventory) == 0:
        product_id = 1
    else:
        product_id = inventory[-1]["id"] + 1
    print("Product ID:", product_id)

    product_name = input("Enter Product Name: ").strip()
    product_price = get_valid_price() #float(input("Enter Product Price: "))
    product_quantity = get_valid_quantity() #int(input("Enter Product Quantity: "))
    product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "quantity": product_quantity
    }
    inventory.append(product)
    save_inventory()
    print("\nProduct Added Successfully!")