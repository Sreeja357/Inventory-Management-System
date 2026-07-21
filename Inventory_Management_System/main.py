from AddProduct import add_product
from ViewProducts import view_products
from SearchProduct import search_product
from UpdateProduct import update_product
from DeleteProduct import delete_product
from StockIn import stock_in
from StockOut import stock_out
from LowStockAlert import low_stock
from InventorySummary import inventory_summary
from file_handler import load_inventory
from file_handler import save_inventory

def menu():
    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Stock In")
    print("7. Stock Out")
    print("8. Low Stock Alert")
    print("9. Inventory Summary")
    print("10. Exit")
load_inventory()
while True:
    menu()
    # choice = int(input("Enter your choice: "))
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice!")
        continue
    if choice == 1:
        add_product()
    elif choice == 2:
        view_products()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        delete_product()
    elif choice == 6:
        stock_in()
    elif choice == 7:
        stock_out()
    elif choice == 8:
        low_stock()
    elif choice == 9:
        inventory_summary()
    elif choice == 10:
        print("Thank You!")
        save_inventory()
        break
    else:
        print("Invalid Choice!")