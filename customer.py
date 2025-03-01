from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import random
import os

class CustWin:
    def __init__(self, root):
        self.root = root
        self.root.title("PG Management System")
        self.root.geometry("1075x535+205+185")

        # Variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar(value="Male")
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar(value="Indian")
        self.var_address = StringVar()
        self.var_id_proof = StringVar(value="Aadhar Card")
        self.var_id_number = StringVar()

        # Title label
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="Aqua", fg="gray", bd=4, relief=RIDGE)
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
        left_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        left_frame.place(x=0, y=50, width=365, height=455)

        # Customer reference label and entry
        lbl_cust_ref = Label(left_frame, text="Customer Ref:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(left_frame, textvariable=self.var_ref, width=22, font=("times new roman", 12, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1, sticky=W)

        # Customer name label and entry
        lbl_cust_name = Label(left_frame, text="Customer Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(left_frame, textvariable=self.var_cust_name, width=22, font=("times new roman", 12, "bold"))
        entry_name.grid(row=1, column=1, sticky=W)

        # Mother name label and entry
        lbl_mother = Label(left_frame, text="Mother Name:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mother.grid(row=2, column=0, sticky=W)
        entry_mother = ttk.Entry(left_frame, textvariable=self.var_mother, width=22, font=("times new roman", 12, "bold"))
        entry_mother.grid(row=2, column=1, sticky=W)

        # Gender label and combobox
        lbl_gender = Label(left_frame, text="Gender:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(left_frame, textvariable=self.var_gender, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Post code
        lbl_postcode = Label(left_frame, text="Post Code:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)
        entry_postcode = ttk.Entry(left_frame, textvariable=self.var_post, width=22, font=("times new roman", 12, "bold"))
        entry_postcode.grid(row=4, column=1, sticky=W)

        # Mobile number
        lbl_mobile = Label(left_frame, text="Mobile Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)
        entry_mobile = ttk.Entry(left_frame, textvariable=self.var_mobile, width=22, font=("times new roman", 12, "bold"))
        entry_mobile.grid(row=5, column=1, sticky=W)

        # Email
        lbl_email = Label(left_frame, text="Email:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)
        entry_email = ttk.Entry(left_frame, textvariable=self.var_email, width=22, font=("times new roman", 12, "bold"))
        entry_email.grid(row=6, column=1, sticky=W)

        # Nationality combobox
        lbl_nationality = Label(left_frame, text="Nationality:", font=("times new roman", 12, "bold"), padx=2, pady=9)
        lbl_nationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(left_frame, textvariable=self.var_nationality, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_nationality["values"] = ("Indian", "American", "British", "Other")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        # ID Proof combobox
        lbl_id_proof = Label(left_frame, text="ID Proof:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_id_proof.grid(row=8, column=0, sticky=W)
        combo_idproof = ttk.Combobox(left_frame, textvariable=self.var_id_proof, font=("arial", 13, "bold"), width=20, state="readonly", cursor="hand1")
        combo_idproof["values"] = ("Aadhar Card", "Driving Licence", "Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        # ID number entry
        lbl_id_number = Label(left_frame, text="ID Number:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)
        entry_id_number = ttk.Entry(left_frame, textvariable=self.var_id_number, width=22, font=("times new roman", 12, "bold"))
        entry_id_number.grid(row=9, column=1, sticky=W)

        # Address entry
        lbl_address = Label(left_frame, text="Address:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)
        entry_address = ttk.Entry(left_frame, textvariable=self.var_address, width=22, font=("times new roman", 12, "bold"))
        entry_address.grid(row=10, column=1, sticky=W)

        # Button frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=390, width=355, height=35)
        Button(btn_frame, text="Add", command=self.add_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=0)
        Button(btn_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=1)
        Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, cursor="hand2").grid(row=0, column=3)

        # Right frame for details table
        right_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        right_frame.place(x=370, y=50, width=700, height=455)

        lbl_SearchBy = Label(right_frame, text="Search By:", font=("arial", 13, "bold"), bg="red", fg="white")
        lbl_SearchBy.grid(row=0, column=0, padx=2, sticky=W)

        combo_Search = ttk.Combobox(right_frame, font=("arial", 13, "bold"), width=15, state="readonly")
        combo_Search["values"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        txt_Search = ttk.Entry(right_frame, width=24, font=("arial", 13, "bold"))
        txt_Search.grid(row=0, column=2, padx=2)

        Button(right_frame, text="Search", command=lambda: self.search_data(txt_Search.get(), combo_Search.get()), font=("arial", 13, "bold"), bg="black", fg="gold", width=8, padx=2, cursor="hand2").grid(row=0, column=3, padx=2)
        Button(right_frame, text="Show All", command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=8, padx=2, cursor="hand2").grid(row=0, column=4, padx=2)

        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=50, width=690, height=380)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.cust_details_table = ttk.Treeview(table_frame, columns=("customer_ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        # Table headings
        self.cust_details_table.heading("customer_ref", text="Customer Ref")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="Post Code")
        self.cust_details_table.heading("mobile", text="Mobile No")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")
        self.cust_details_table["show"] = "headings"

        # Column widths
        self.cust_details_table.column("customer_ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)

        # Bind event
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch data
        self.fetch_data()

    # for add button
    def add_data(self):
        if self.var_cust_name.get()=="" and self.var_mother.get()=="" and self.var_post.get()=="" and self.var_mobile.get()=="" and self.var_email.get()=="" and self.var_id_number.get()=="" and self.var_address.get():
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customers VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success", "Customer Has Been Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    
    # for fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customers")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # on click data will be filled from customers table using customer ref
    def get_cursor(self, event=""):
        cursor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    # for update button
    def update_data(self):
        if self.var_cust_name.get()=="" and self.var_mother.get()=="" and self.var_post.get()=="" and self.var_mobile.get()=="" and self.var_email.get()=="" and self.var_id_number.get()=="" and self.var_address.get():
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customers SET Name=%s, Mother=%s, Gender=%s, Post=%s, Mobile=%s, Email=%s, Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE customer_ref=%s", (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()
            messagebox.showinfo("Update", "Customer Details Has Been Updated Successfully", parent=self.root)

    # for delete button
    def delete_data(self):
        delete = messagebox.askyesno("Delete", "Do you want to delete this customer?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
            my_cursor = conn.cursor()
            query = "DELETE FROM customers WHERE customer_ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fetch_data()
            self.reset_data()

    # for reset button and always give new customer ref
    def reset_data(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Indian")
        self.var_id_proof.set("Aadhar Card")
        self.var_id_number.set("")
        self.var_address.set("")

    # for Search data by using mobile and customer ref
    def search_data(self, search_text, search_by):
        conn = mysql.connector.connect(host="localhost", username="root", password="2004", database="management")
        my_cursor =conn.cursor()
        if search_by == "Mobile":
            query = "SELECT * FROM customers WHERE Mobile LIKE %s"
        else:  # Search by "Ref"
            query = "SELECT * FROM customers WHERE customer_ref LIKE %s"
        my_cursor.execute(query, (f"%{search_text}%",))
        rows = my_cursor.fetchall()
        
        if rows:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for row in rows:
                self.cust_details_table.insert("", END, values=row)
        else:
            messagebox.showinfo("Info", "No matching records found.")
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CustWin(root)
    root.mainloop()