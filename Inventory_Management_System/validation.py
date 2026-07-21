def get_valid_price():
    while True:
        try:
            product_price = float(input("Enter Product Price: "))
            if product_price >= 0:
                return product_price
            else:
                print("Price cannot be negative.")
        except ValueError:
            print("Invalid Price. Please enter a valid number.")

def get_valid_quantity():
    while True:
        try:
            product_quantity = int(input("Enter Product Quantity: "))
            if product_quantity >= 0:
                return product_quantity
            else:
                print("Quantity cannot be negative.")
        except ValueError:
            print("Invalid Quantity. Please enter a whole number.")