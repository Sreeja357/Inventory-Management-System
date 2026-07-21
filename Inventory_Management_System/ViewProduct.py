from data import inventory

def view_products():
    print("\n========== PRODUCT LIST ==========")
    if len(inventory) == 0:
        print("No products available.")
        return
    print("-" * 55)
    print(f"{'ID':<10}{'Name':<15}{'Price':<15}{'Quantity':<10}")
    print("-" * 55)
    for product in inventory:
        print(f"{product['id']:<10}{product['name']:<15}{product['price']:<15}{product['quantity']:<10}")
    print("-" * 55)