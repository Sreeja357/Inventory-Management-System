from data import inventory

def inventory_summary():
    print("\n----- Inventory Summary -----")
    total_products = len(inventory)
    total_quantity = 0
    total_value = 0
    for product in inventory:
        total_quantity += product["quantity"]
        total_value += product["price"] * product["quantity"]
    print(f"Total Products      : {total_products}")
    print(f"Total Quantity      : {total_quantity}")
    print(f"Total Inventory Value : ₹{total_value:.2f}")