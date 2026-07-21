from data import inventory
from file_handler import save_inventory

def delete_product():
    print("\n----- Delete Product -----")
    delete_id = int(input("Enter Product ID to Delete: "))
    for product in inventory:
        if product["id"] == delete_id:
            inventory.remove(product)
            save_inventory()
            print("\nProduct Deleted Successfully.")
            return
    print("\nProduct Not Found.")