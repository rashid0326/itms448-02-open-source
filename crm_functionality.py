import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to add a new customer to the database
def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "Please fill in all fields", width=300, height=150)
        return

    # Connect to SQLite database
    conn = sqlite3.connect('crm_database.db')
    cursor = conn.cursor()

    # Insert customer data into the database
    cursor.execute("INSERT INTO customers (name, email, phone, address) VALUES (?, ?, ?, ?)", (name, email, phone, address))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer added successfully", width=300, height=150)

# Function to update customer information
def update_customer():
    # Placeholder for updating customer information
    messagebox.showinfo("Info", "Update functionality placeholder", width=300, height=150)

# Function to track customer interactions
def track_interactions():
    # Placeholder for tracking interactions
    messagebox.showinfo("Info", "Track interactions placeholder", width=300, height=150)

# Function for personalized experiences
def personalized_experience():
    # Placeholder for personalized experiences
    messagebox.showinfo("Info", "Personalized experiences placeholder", width=300, height=150)

# Create main window with a larger size
window = tk.Tk()
window.title("Customer Relationship Management System")
window.geometry("800x600")  # Width x Height

# Create labels and entry fields for customer information
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Email:").pack()
email_entry = tk.Entry(window)
email_entry.pack()

tk.Label(window, text="Phone:").pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

tk.Label(window, text="Address:").pack()
address_entry = tk.Entry(window)
address_entry.pack()

# Buttons for various functionalities
add_button = tk.Button(window, text="Add Customer", command=add_customer)
add_button.pack()

update_button = tk.Button(window, text="Update Customer", command=update_customer)
update_button.pack()

track_button = tk.Button(window, text="Track Interactions", command=track_interactions)
track_button.pack()

personalized_button = tk.Button(window, text="Personalized Experience", command=personalized_experience)
personalized_button.pack()

# Run the main loop
window.mainloop()
