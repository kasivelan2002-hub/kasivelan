# ☕ Cafe Invoice System (Python + Tkinter + MySQL)

## 📌 Project Overview

This project is a **Cafe Invoice Management System** built using **Python Tkinter** for the graphical user interface and **MySQL** for database storage.

The application allows users to:

* Register and Login securely
* Place food orders
* Automatically calculate bill amount
* Store and display records from database
* Submit customer feedback
* View menu prices

This system is suitable for small cafes and learning database-connected GUI applications.

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI Interface
* **MySQL** – Database
* **mysql-connector-python**
* **OS, Time, Random Libraries**

---

## 🚀 Features

### 🔐 Login & Registration

* New users can register with username, password, and name.
* Existing users can log in using credentials stored in MySQL.
* Empty fields validation.
* Successful login opens the main Cafe Invoice System.

---

### 🍩 Food Ordering System

Users can enter quantity for:

* Muffin (₹160)
* Brownie (₹150)
* Doughnut (₹100)
* Coffee (₹75)

The system automatically calculates:

* Cost
* Subtotal
* Tax (18%)
* Service Charge
* Total Amount

---

### 💾 Database Management

* Orders are stored in MySQL table (`records`).
* Displays all records in a table view (TreeView).
* Users can add new orders.
* Delete selected records.
* Data persists even after restarting the app.

---

### 📋 Menu Card

Displays the price list of all food items in a separate window.

---

### ⭐ Feedback Form

* Customers can submit:

  * Name
  * Email
  * Rating (Excellent, Good, Average, Poor)
  * Comments
* Feedback is stored in the database.

---

## 🖥️ Installation & Setup

### ✅ Prerequisites

1. Install Python 3
2. Install MySQL Server
3. Install required library:

```bash
pip install mysql-connector-python
```

---

### ✅ Database Setup

Create a MySQL database named:

```
jones
```

Create tables as needed (or the program will auto-create them):

* login
* jp_cafe
* records
* feedback

Update MySQL credentials in the code if needed:

```python
host="localhost"
user="root"
password=""
database="jones"
```

---

### ▶️ How to Run

1. Clone or download the repository.
2. Open terminal in project folder.
3. Run the program:

```bash
python main.py
```

(Login window will appear.)

---

## 📷 Output Screens

* Signup Page
* Login Page
* Cafe Invoice System Dashboard
* Menu Card
* Feedback Form

---

## ⚠️ Notes

* Ensure MySQL service is running.
* Database name must match exactly (`jones`).
* Internet connection is not required.
* Designed for educational and small-scale usage.

---

## 🙌 Author

**Kasivelan S**

---

If you want, I can also:
✅ Shorten this README
✅ Add screenshots section
✅ Make it more professional for portfolio
✅ Convert to markdown file

Just tell me 👍
