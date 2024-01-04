import tkinter as tk
from tkinter import ttk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="florist_shop"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def enter_data():
    # customer and booking detail
   name = first_name_entry.get()
   phone_number = phone_number_entry.get()
   address = address_entry.get()
   bouquet = bouquet_combobox.get()
   quantity = int (quantity_entry.get())
   

    #  the price below is to defined the value from your selections
   prices = {
        "Birthday": 50,
        "Anniversary": 100,
        "Graduation": 70,
    }
   
   # calculate total price.
   total_price = (prices[bouquet] * quantity)

   sql = "INSERT INTO booking_detail (Name, Phone_Number, Address, Bouquet_type, Quantity, Total_price) VALUES (%s, %s, %s, %s, %s, %s)"
   val = (name,phone_number, address, bouquet, quantity, total_price)
   mycursor.execute(sql, val)
   mydb.commit()

   # print out the output
   output_label.config(text=f"Name: {name}, Phone Number: {phone_number}, Address: {address} Bouquet: {bouquet}, Quantity: {quantity}, Total Price: RM{total_price}")


   print("Name: ", name, "Phone Number: ", phone_number, "Address: ", address)
   print("Bouquet: ", bouquet, "Quantity: ", quantity)


# Your Main window, You need to have the title.
root = tk.Tk()
root.title("Florist Shop")


frame = tk.Frame(root)
frame.pack()

# Save customer info
cust_info_frame =tk.LabelFrame(frame, text="Customer and Booking Detail")
cust_info_frame.grid(row= 0, column=0, padx=40, pady=30)

first_name_label =tk.Label (cust_info_frame, text= "Name")
first_name_label.grid(row= 0, column=0)
phone_number_label = tk.Label (cust_info_frame, text= "Phone Number")
phone_number_label.grid(row= 1, column=0)
address_label =tk.Label (cust_info_frame, text= "Address")
address_label.grid(row=2, column= 0)

first_name_entry = tk.Entry(cust_info_frame)
phone_number_entry = tk.Entry(cust_info_frame)
address_entry =tk.Entry(cust_info_frame)
first_name_entry.grid(row= 0, column= 1)
phone_number_entry.grid(row=1, column=1)
address_entry.grid (row=2, column=1)

bouquet_label = tk.Label(cust_info_frame, text="Choose your Bouquet")
bouquet_combobox = ttk.Combobox(cust_info_frame, values=["Birthday", "Anniversary", "Graduation"])
bouquet_label.grid(row=0, column=2)
bouquet_combobox.grid(row=1, column=2)

# Quantity Entry. Label and cust can insert data thru entry
quantity_label = tk.Label(cust_info_frame, text="Quantity:")
quantity_label.grid(row=2, column=2)
quantity_entry = tk.Entry(cust_info_frame)
quantity_entry.grid(row=3, column=2)

for widget in cust_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Page Title
label = tk.Label(root, text='Flower Bouquet Price', font=("Times New Romans",14, "bold"))
label.pack(ipadx=5, ipady=5)

# Prices List by using textbox
prices_text = tk.Text(root, height=10, width=30)
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "Bouquet & Prices:\n\n")
prices_text.insert(tk.END, "Birthday Bouquet \nPrice: RM50\n\n")
prices_text.insert(tk.END, "Anniversary Bouquet \nPrice: RM100\n\n")
prices_text.insert(tk.END, "Graduation Bouquet\nPrice: RM70\n\n")
prices_text.configure(state='disabled')

# Save Button
save_button = tk.Button(root, text="Calculate", command= enter_data)
save_button.pack(pady=10)

label = tk.Label(root, text='Detail and Price Bouquet', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=20)
output_label = tk.Label(root, text="")
output_label.pack()


root.mainloop()