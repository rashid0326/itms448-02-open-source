import tkinter as tk
from tkinter import messagebox
import api_integration
import crm_functionality

# Create main window
window = tk.Tk()
window.title("CRM System")

# Set window size to match GUI
window.geometry("600x400")  # Width x Height

# Force window update to synchronize sizes
window.update_idletasks()

# Initialize database connection
# Replace 'initialize_database_connection()' with actual database connection initialization code
def initialize_database_connection():
    # Placeholder for initializing database connection
    pass

initialize_database_connection()

# Function to handle GUI interactions
def handle_add_customer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if not name or not email or not phone or not address:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Call CRM function to add customer
    crm_functionality.add_customer(name, email, phone, address)
    messagebox.showinfo("Success", "Customer added successfully")

# Labels and entry fields for customer information
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

# Button to add customer
add_button = tk.Button(window, text="Add Customer", command=handle_add_customer)
add_button.pack()

# Call API integration functions
# Replace placeholders with actual API calls using api_integration module
api_data = api_integration.get_google_maps_data("New York")
print(api_data)  # Placeholder for testing API data retrieval

# Run the main loop
window.mainloop()
