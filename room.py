from tkinter import *
from tkinter import ttk, messagebox
from mysqlx import Row
from tkcalendar import Calendar
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import os

class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("PG MANAGEMENT SYSTE")
        self.root.geometry("1075x535+205+185")

        # Variables
        self.var_ref = StringVar()
        self.var_room_number = StringVar()
        self.var_mobile = StringVar()
        self.var_check_in = StringVar()
        self.var_no_of_months = StringVar(value="1 Month")
        self.var_checkout = StringVar()
        self.var_room_type = StringVar(value="Single")
        self.var_available_room = StringVar()
        self.var_meal_option = StringVar(value="None")
        self.var_meal_price = StringVar(value="0")  # Default price for None
        self.var_total_price = StringVar(value="0")  # Total price variable

        # Room prices
        self.room_prices = {
            "Single": 3000,
            "Double": 4500,
            "Suite": 8000
        }

        # Meal prices based on selection
        self.meal_prices = {
            "None": 0,
            "Veg": 1000,      
            "Non-Veg": 1500
        }

        # Title label
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="Aqua", fg="gray", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1075, height=50)

        # Logo image
        img = Image.open(os.path.join("images", "LOGO.png"))
        img = img.resize((100, 50), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Left logo
        lblimg_left = Label(self.root, image=self.photoimg, bd=4, bg="Aqua", relief=RIDGE)
        lblimg_left.place(x=0, y=0, width=100, height=50)

        # Right logo
        lblimg_right = Label(self.root, image=self.photoimg, bd=4, bg="Aqua", relief=RIDGE)
        lblimg_right.place(x=975, y=0, width=100, height=50)

        # Left frame for customer details
        left_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        left_frame.place(x=0, y=50, width=365, height=455)

        #cust ref
        lbl_cust_ref = Label(left_frame, text="Customer Ref:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(left_frame, textvariable=self.var_ref, width=13, font=("times new roman", 12, "bold"))
        entry_ref.grid(row=0, column=1, sticky=W)

        # Fetch Button
        btnFetch = Button(left_frame, text="Fetch Data", command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2")
        btnFetch.place(x=250, y=0, width=100, height=35)

        #Room
        lbl_room_number = Label(left_frame, text="Room Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room_number.grid(row=1, column=0, sticky=W)
        entry_room_number = ttk.Entry(left_frame, textvariable=self.var_room_number, width=13, font=("times new roman", 12, "bold"))
        entry_room_number.grid(row=1, column=1, sticky=W)

        # Mobile number
        lbl_mobile = Label(left_frame, text="Mobile Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=2, column=0, sticky=W)
        entry_mobile = ttk.Entry(left_frame, textvariable=self.var_mobile, width=25, font=("times new roman", 12, "bold"), state='readonly')
        entry_mobile.grid(row=2, column=1, sticky=W)

        # Check in label and button for calendar popup
        lbl_check_in = Label(left_frame, text="Check-In Date:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_check_in.grid(row=3, column=0, sticky=W)

        self.lbl_check_in_date = Label(left_frame, text="", font=("times new roman", 12, "bold"), relief=SUNKEN, width=15)
        self.lbl_check_in_date.grid(row=3, column=1, sticky=W)

        # Create a button to open the calendar
        btn_calendar = Button(left_frame, text="Select Date", command=self.open_calendar, font=("arial", 10, "bold"), bg="lightblue", fg="black", cursor="hand2")
        btn_calendar.place(x=270, y=105, width=80, height=30)

        # Months label and combobox
        lbl_month = Label(left_frame, text="Months:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_month.grid(row=4, column=0, sticky=W)
        combo_months = ttk.Combobox(left_frame, textvariable=self.var_no_of_months, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_months["values"] = ("1 Month", "2 Months", "3 Months", "6 Months", "12 Months")
        combo_months.current(0)
        combo_months.grid(row=4, column=1)
        combo_months.bind("<<ComboboxSelected>>", self.calculate_checkout)

        # Checkout label
        lbl_checkout = Label(left_frame, text="Check-Out Date:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_checkout.grid(row=5, column=0, sticky=W)
        self.lbl_checkout_date = Label(left_frame, text="", font=("times new roman", 12, "bold"), relief=SUNKEN, width=18)
        self.lbl_checkout_date.grid(row=5, column=1, sticky=W)

        # Room Type label and combobox
        lbl_room_type = Label(left_frame, text="Room Type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=6, column=0, sticky=W)
        combo_room_type = ttk.Combobox(left_frame, textvariable=self.var_room_type, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_room_type["values"] = ("Single", "Double", "Suite")
        combo_room_type.current(0)
        combo_room_type.grid(row=6, column=1)
        combo_room_type.bind("<<ComboboxSelected>>", self.update_price)

        # Meal Option label and combobox
        lbl_meal_option = Label(left_frame, text="Meal Option:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal_option.grid(row=10, column=0, sticky=W)

        combo_meal_option = ttk.Combobox(left_frame, textvariable=self.var_meal_option, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_meal_option["values"] = ("None", "Veg", "Non-Veg")
        combo_meal_option.current(0)
        combo_meal_option.grid(row=10, column=1)
        combo_meal_option.bind("<<ComboboxSelected>>", self.update_meal_price)

        # Meal Price label
        lbl_meal_price = Label(left_frame, text="Meal Price:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_meal_price.grid(row=11, column=0, sticky=W)

        # Display meal price
        lbl_display_meal_price = Label(left_frame, textvariable=self.var_meal_price, font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_display_meal_price.grid(row=11, column=1, sticky=W)

        # Total Price label
        lbl_total_price = Label(left_frame, text="Total Price:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_total_price.grid(row=12, column=0, sticky=W)

        # Display total price
        lbl_display_total_price = Label(left_frame, textvariable=self.var_total_price, font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_display_total_price.grid(row=12, column=1, sticky=W)

        # Button
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=390, width=355, height=35)
        Button(btn_frame, text="Add", command=self.add_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=0)
        Button(btn_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=1)
        Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=3)

        # Mid-up frame for customer details
        mid_up = LabelFrame(self.root, bd=2, relief=RIDGE, text="Fetch Data", fg="Gray", padx=2, font=("times new roman", 12, "bold"),bg="aqua")
        mid_up.place(x=365, y=50, width=200, height=200)

        # Text widget to display fetched data
        self.data_display = Text(mid_up, font=("arial", 12), bg="lightyellow", wrap=WORD)
        self.data_display.pack(expand=True, fill=BOTH)
        self.data_display.config(state=DISABLED)  # Set the Text widget to read-only

        # Fetch Data Button
        btn_fetch_all = Button(mid_up, text="Fetch All Data", command=self.fetch_all_customers, font=("arial", 10, "bold"), bg="blue", fg="white", cursor="hand2")
        btn_fetch_all.pack(side=BOTTOM, fill=X)

        
        #right up frame
        right_up = LabelFrame(self.root, bd=2, relief=RIDGE)
        right_up.place(x=570, y=50, width=505, height=200)

        img2 = Image.open(os.path.join("images", "pg3.jpg"))
        img2 = img2.resize((510, 195), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(right_up, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=510, height=195)

        # Right frame
        right_down = LabelFrame(self.root, bd=2, relief=RIDGE, text="Detail view and search system", fg="Gray", padx=2, font=("times new roman", 12, "bold"),bg="aqua")
        right_down.place(x=370, y=250, width=705, height=255)

        btn1_frame1 = Frame(right_down, bd=2, relief=RIDGE, border=0.5)
        btn1_frame1.place(x=0, y=0, width=695, height=36)

        lbl_SearchBy = Label(btn1_frame1, text="Search By:", font=("arial", 13, "bold"), bg="red", fg="white")
        lbl_SearchBy.grid(row=0, column=0, padx=2, sticky=W)

        combo_Search = ttk.Combobox(btn1_frame1, font=("arial", 13, "bold"), width=15, state="readonly")
        combo_Search["values"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        txt_Search = ttk.Entry(btn1_frame1, width=21, font=("arial", 13, "bold"))
        txt_Search.grid(row=0, column=2, padx=2)

        Button(btn1_frame1, text="Search", command=lambda: self.search_data(txt_Search.get(), combo_Search.get()), font=("arial", 13, "bold"), bg="black", fg="gold", width=10, padx=2, cursor="hand2").grid(row=0, column=3, padx=2)
        Button(btn1_frame1, text="Show All", command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=10, padx=2, cursor="hand2").grid(row=0, column=4, padx=2)

        # Table frame
        table_frame = Frame(right_down, bd=2, relief=RIDGE, border=2)
        table_frame.place(x=0, y=40, width=700, height=190)


        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.room_details_table = ttk.Treeview(table_frame, columns=("customer_ref", "room_number", "mobile", "check_in", "duration", "check_out", "room_type", "meal_plan", "meal_price", "total_price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)

        # Table headings
        self.room_details_table.heading("customer_ref", text="Customer Ref")
        self.room_details_table.heading("room_number", text="Room No")
        self.room_details_table.heading("mobile", text="Mobile")
        self.room_details_table.heading("check_in", text="Check-In Date")
        self.room_details_table.heading("duration", text="Duration")
        self.room_details_table.heading("check_out", text="Check-Out Date")
        self.room_details_table.heading("room_type", text="Room Type")
        self.room_details_table.heading("meal_plan", text="Meal Plan")
        self.room_details_table.heading("meal_price", text="Meal Price")
        self.room_details_table.heading("total_price", text="Total Price")
        self.room_details_table["show"] = "headings"

        # Column widths
        self.room_details_table.column("room_number", width=100)
        self.room_details_table.column("customer_ref", width=100)
        self.room_details_table.column("mobile", width=100)
        self.room_details_table.column("check_in", width=100)
        self.room_details_table.column("duration", width=80)
        self.room_details_table.column("check_out", width=100)
        self.room_details_table.column("room_type", width=100)
        self.room_details_table.column("meal_plan", width=100)
        self.room_details_table.column("meal_price", width=100)
        self.room_details_table.column("total_price", width=120)
        self.room_details_table.pack(fill=BOTH, expand=1)

        # Bind event
        self.room_details_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch data
        self.fetch_room_data()


    # on click fetch data from customer ref 
    def fetch_data(self):
        """Fetch customer data based on customer ref."""
        customer_ref = self.var_ref.get()
        if not customer_ref:
            messagebox.showerror("Error", "Please enter a Customer Reference number.")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="2004", database="management")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE customer_ref = %s", (customer_ref,))
            row = cursor.fetchone()
            conn.close()

            if row:
                self.var_mobile.set(row[5])  # Assuming mobile is in the 5th column
                self.data_display.config(state=NORMAL)
                self.data_display.delete(1.0, END)
                self.data_display.insert(END, f"Customer Ref: {row[0]}\n")
                self.data_display.insert(END, f"Name: {row[1]}\n")
                self.data_display.insert(END, f"Email: {row[6]}\n")
                self.data_display.insert(END, f"Mobile: {row[5]}\n")
                self.data_display.config(state=DISABLED)
            else:
                messagebox.showerror("Error", "No data found for this reference.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # fetch data show on mid frame
    def fetch_all_customers(self):
        """Fetch all customer data and display it in the mid-up frame."""
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="2004", database="management")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers")
            rows = cursor.fetchall()
            conn.close()

            self.data_display.config(state=NORMAL)
            self.data_display.delete(1.0, END)
            for row in rows:
                self.data_display.insert(END, f"Ref: {row[0]}, Name: {row[1]} {row[2]}, Mobile: {row[4]}\n\n")
            self.data_display.config(state=DISABLED)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # fetch all room detil after add or update or delete
    def fetch_room_data(self):
        """Fetch all room details in right down frame"""
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room_details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()



    # for fill data in booking form
    def get_cursor(self, event):
        # Fetch selected row information
        cursor_row = self.room_details_table.focus()
        content = self.room_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_room_number.set(row[1])
        self.var_mobile.set(row[2])

    # select date on calender for check-in date 
    def open_calendar(self):
        def get_date():
            selected_date = calendar.selection_get()
            self.var_check_in.set(selected_date)
            self.lbl_check_in_date.config(text=selected_date.strftime("%Y-%m-%d"))
            self.calculate_checkout()
            calendar_window.destroy()

        calendar_window = Toplevel(self.root)
        calendar_window.title("Select Check-In Date")
        calendar = Calendar(calendar_window, selectmode='day', year=2024, month=11, day=4)
        calendar.pack(padx=20, pady=20)

        btn_select = Button(calendar_window, text="Select Date", command=get_date)
        btn_select.pack(pady=10)

    # calculate check-out date after selecting check-in date and months
    def calculate_checkout(self, event):
        """Calculate checkout date based on check-in date and duration."""
        try:
            check_in_date = datetime.strptime(self.lbl_check_in_date.cget("text"), "%Y-%m-%d")
            duration_months = int(self.var_no_of_months.get().split()[0])  # Get the number of months
            checkout_date = check_in_date + timedelta(days=duration_months * 30)  # Roughly calculate checkout date
            self.var_checkout.set(checkout_date.strftime("%Y-%m-%d"))
            self.lbl_checkout_date.config(text=self.var_checkout.get())
            self.update_total_price()  # Update total price whenever checkout changes
        except ValueError:
            messagebox.showerror("Error", "Please select a valid check-in date first.")

    # add room_price and meal_price than multiply with selected months
    # calculate the total price 
    def update_total_price(self):
        """Update the total price based on room type, meal option, and duration."""
        try:
            room_price = self.room_prices[self.var_room_type.get()]
            meal_price = self.meal_prices[self.var_meal_option.get()]
            duration_months = int(self.var_no_of_months.get().split()[0])  # Get the number of months
            total_price = (room_price + meal_price) * duration_months
            self.var_total_price.set(str(total_price))
        except KeyError:
            self.var_total_price.set("0")


    def update_price(self, event=None):
        room_type = self.var_room_type.get()
        meal_option = self.var_meal_option.get()
        
        # Calculate room and meal prices
        room_price = self.room_prices.get(room_type, 0)
        meal_price = self.meal_prices.get(meal_option, 0)
        
        # Get the number of months as an integer
        number_of_months = int(self.var_no_of_months.get().split()[0])
        
        # Calculate total price based on number of months
        total_price = (room_price + meal_price) * number_of_months
        
        # Update price display
        self.var_meal_price.set(meal_price)
        self.var_total_price.set(total_price)


    def update_meal_price(self, event=None):
        self.update_price()

    # for add button
    def add_data(self):
        """Add customer and booking details to the database and update room status."""
        # Here you would gather all necessary details from the form.
        customer_ref = self.var_ref.get()
        room_number = self.var_room_number.get()
        mobile = self.var_mobile.get()
        check_in = self.lbl_check_in_date.cget("text")
        check_out = self.lbl_checkout_date.cget("text")
        room_type = self.var_room_type.get()
        duration = self.var_no_of_months.get()
        meal_option = self.var_meal_option.get()
        meal_price = self.var_meal_price.get()
        total_price = self.var_total_price.get()

        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="2004", database="management")
            cursor = conn.cursor()
            # Insert booking data
            cursor.execute("INSERT INTO room_details (customer_ref, room_number, mobile, check_in,duration, check_out, room_type,  meal_plan, meal_price, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (customer_ref, room_number, mobile, check_in, duration,  check_out, room_type,meal_option, meal_price, total_price))

            conn.commit()
            self.fetch_room_data()
            self.reset_data()
            conn.close()

            messagebox.showinfo("Success", "Room booked successfully!", parent=self.root)
            self.fetch_room_data()  # Refresh the available rooms list
            self.reset_data()  # Reset form fields after booking
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            
    # for update button
    def update_data(self):
        if self.var_check_in.get() == "" or self.var_checkout.get() == "":
            messagebox.showerror("Error", "Please Select Check-in date or months", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="2004",
                    database="management"
                )
                my_cursor = conn.cursor()
                # Corrected SQL syntax for the UPDATE statement
                my_cursor.execute("""
                    UPDATE room_details SET 
                        room_number=%s, 
                        mobile=%s, 
                        check_in=%s, 
                        check_out=%s, 
                        room_type=%s, 
                        duration=%s, 
                        meal_plan=%s, 
                        meal_price=%s, 
                        total_price=%s 
                    WHERE customer_ref=%s
                """, (
                    self.var_room_number.get(),
                    self.var_mobile.get(),
                    self.var_check_in.get(),
                    self.var_checkout.get(),
                    self.var_room_type.get(),
                    self.var_no_of_months.get(),
                    self.var_meal_option.get(),
                    self.var_meal_price.get(),
                    self.var_total_price.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_room_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo("Success", "Room booked successfully!", parent=self.root)
                self.fetch_room_data()  # Refresh the available rooms list
                self.reset_data()  # Reset form fields after booking
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)


    # for delete button
    def delete_data(self):
        """Delete customer data based on customer ref."""
        delete = messagebox.askyesno("Delete", "Do you want to delete this?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
            my_cursor = conn.cursor()
            query = "DELETE FROM room_details WHERE customer_ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_room_data()
            conn.close()
            self.reset_data()

    # for reset button 
    def reset_data(self):
        """Reset all fields to their default values."""
        self.var_ref.set("")
        self.var_mobile.set("")
        self.var_check_in.set("")
        self.var_no_of_months.set("1 Month")
        self.var_checkout.set("")
        self.var_room_type.set("Single")
        self.var_available_room.set("")
        self.var_meal_option.set("None")
        self.var_meal_price.set("0")
        self.var_total_price.set("0")
        self.var_room_number.set("")
        
        # Reset displayed labels
        self.lbl_check_in_date.config(text="")
        self.lbl_checkout_date.config(text="")

    # for searching the data
    def search_data(self, search_text, search_by):
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
        my_cursor = conn.cursor()
        if search_by == "Mobile":
            query = "SELECT * FROM customers WHERE Mobile LIKE %s"
        else:  # Search by "Ref"
            query = "SELECT * FROM customers WHERE customer_ref LIKE %s"
        my_cursor.execute(query, (f"%{search_text}%",))
        rows = my_cursor.fetchall()
        
        if rows:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for row in rows:
                self.room_details_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Info", "No matching records found.")
            conn.commit()
        conn.close()
 

if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()