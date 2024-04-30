import tkinter as tk
from tkinter import messagebox
import sqlite3

def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Connect to SQLite database
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()

    # Insert customer data into the database
    cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)", (name, email, phone, address))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer added successfully")

# Create main window
window = tk.Tk()
window.title("Customer Relationship Management System")

# Set window size
window.geometry("600x400")  # Width x Height

# Create labels and entry fields for customer information
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window, width=50)  # Increased width to 50 characters
name_entry.pack()

tk.Label(window, text="Email:").pack()
email_entry = tk.Entry(window, width=50)  # Increased width to 50 characters
email_entry.pack()

tk.Label(window, text="Phone:").pack()
phone_entry = tk.Entry(window, width=50)  # Increased width to 50 characters
phone_entry.pack()

tk.Label(window, text="Address:").pack()
address_entry = tk.Entry(window, width=100)  # Increased width to 100 characters
address_entry.pack()

# Button to add customer
add_button = tk.Button(window, text="Add Customer", command=add_customer)
add_button.pack()

# Run the main loop
window.mainloop()
