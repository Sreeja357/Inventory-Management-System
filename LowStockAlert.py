from data import inventory

def low_stock():
    print("\n----- Low Stock Alert -----")
    found = False
    for product in inventory:
        if product["quantity"] < 5:
            if found == False:
                print("-" * 55)
                print(f"{'ID':<10}{'Name':<20}{'Price':<10}{'Quantity':<10}")
                print("-" * 55)
                found = True
            print(f"{product['id']:<10}{product['name']:<20}{product['price']:<10}{product['quantity']:<10}")
    if found == False:
        print("No Low Stock Products.")