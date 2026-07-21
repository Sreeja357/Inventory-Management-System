# 📦 Inventory Management System
A simple **Python-based Inventory Management System** that allows users to manage product inventory efficiently. The application is built using **functional programming**, stores data in a **JSON file**, and provides an easy-to-use console interface.

---

## 🚀 Features

- ➕ Add Product (Auto-generated Product ID)
- 📋 View All Products
- 🔍 Search Product (By ID & Name)
- ✏️ Update Product Details
- ❌ Delete Product
- 📦 Stock In (Increase Quantity)
- 📤 Stock Out (Decrease Quantity)
- ⚠️ Low Stock Alert
- 📊 Inventory Summary
- 💾 JSON File Storage (Data Persistence)
- ✅ Input Validation for Price and Quantity
- 🛡️ Exception Handling

---

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling
- Exception Handling
- Modular Programming

---

## 📁 Project Structure

```
Inventory_Management_System/
│
├── main.py
├── data.py
├── file_handler.py
├── validation.py
├── inventory.json
│
├── add_product.py
├── view_products.py
├── search_product.py
├── update_product.py
├── delete_product.py
├── stock_in.py
├── stock_out.py
├── low_stock.py
└── summary.py
```

---

## ⚙️ Requirements

- Python 3.x

No external libraries are required.

---

## ▶️ How to Run

1. Clone or download the project.
2. Open the project folder in VS Code or any Python IDE.
3. Open a terminal.
4. Run:

```bash
python main.py
```

---

## 📌 Menu Options

```
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Stock In
7. Stock Out
8. Low Stock Alert
9. Inventory Summary
0. Exit
```

---

## 💡 Key Features

### Auto-generated Product ID
Each product is automatically assigned a unique Product ID.

### Data Persistence
Inventory data is stored in `inventory.json`, ensuring data is saved even after the application is closed.

### Input Validation
The system validates:
- Product Price
- Product Quantity

to prevent invalid or negative values.

### Low Stock Alert
Displays products whose quantity falls below the defined threshold.

### Inventory Summary
Displays:
- Total Products
- Total Quantity
- Total Inventory Value

---

## 🎯 Learning Outcomes

This project demonstrates:

- Functions
- Modular Programming
- CRUD Operations
- JSON File Handling
- Exception Handling
- Input Validation
- Python Data Structures (List & Dictionary)

---

## 📷 Sample Output

```
----- Inventory Management System -----

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Stock In
7. Stock Out
8. Low Stock Alert
9. Inventory Summary
0. Exit

Enter your choice:
```

---

## 👨‍💻 Author

**Sasanooru Sreeja**

B.Tech - Computer Science & Engineering

Python Project – Inventory Management System

---

## 📄 License

This project is created for educational and learning purposes.
