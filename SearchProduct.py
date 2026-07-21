from data import inventory

def search_product():
    print("\n----- Search Product -----")
    print("1. Search by Product ID")
    print("2. Search by Product Name")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        search_by_id()
    elif choice == 2:
        search_by_name()
    else:
        print("Invalid Choice!")

def search_by_id():
    search_id = int(input("Enter Product ID: "))
    for product in inventory:
        if product["id"] == search_id:
            print("\nProduct Found")
            print("-" * 30)
            print("Product ID      :", product["id"])
            print("Product Name    :", product["name"])
            print("Product Price   :", product["price"])
            print("Product Quantity:", product["quantity"])
            print("-" * 30)
            return
    print("\nProduct Not Found.")

def search_by_name():
    search_name = input("Enter Product Name: ").strip().lower()
    found = False
    for product in inventory:
        if search_name in product["name"].lower():
            print("-" * 30)
            print("Product ID      :", product["id"])
            print("Product Name    :", product["name"])
            print("Product Price   :", product["price"])
            print("Product Quantity:", product["quantity"])
            print("-" * 30)
            found = True
    if not found:
        print("\nProduct Not Found.")
    # # search_id = int(input("Enter Product ID to Search: "))
    # search_name = input("Enter Product Name: ").strip().lower()
    # for product in inventory:
    #     if product["name"].lower() == search_name:
    #         print("\nProduct Found")
    #         print("-" * 30)
    #         print("Product ID      :", product["id"])
    #         print("Product Name    :", product["name"])
    #         print("Product Price   :", product["price"])
    #         print("Product Quantity:", product["quantity"])
    #         print("-" * 30)
    #         return
    # print("\nProduct Not Found.")