from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import os

class Details_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Meal Plan")
        self.root.geometry("1075x535+205+185")

        # Title label
        lbl_title = Label(self.root, text="Weekly Meal Plan and Rooms  View", font=("times new roman", 18, "bold"), bg="Aqua", fg="gray")
        lbl_title.pack(side=TOP, fill=X)

        # Left frame for meal plan details
        left_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Meal Plan Details", bg="light blue",fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        left_frame.place(x=5, y=35, width=500, height=250)

        # Treeview for displaying meal plan
        self.tree = ttk.Treeview(left_frame, columns=("Day", "Meal Type", "Details"), show="headings")
        self.tree.heading("Day", text="Day")
        self.tree.heading("Meal Type", text="Meal Type")
        self.tree.heading("Details", text="Details")
        self.tree.column("Day", width=70)
        self.tree.column("Meal Type", width=50)
        self.tree.column("Details", width=200)
        self.tree.pack(fill=BOTH, expand=False)

        # Connect to database and fetch meal plan data
        self.fetch_data()

        # Right frame for single  room view
        mid = LabelFrame(self.root, bd=2, relief=RIDGE, text="Single Room",  bg="light blue", fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        mid.place(x=507, y=35, width=278, height=250)

        # Single room image
        img = Image.open(os.path.join("images", "single.png"))
        img = img.resize((270, 225), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        lblimg_left = Label(mid, image=self.photoimg, bg="aqua", bd=4,relief=RIDGE)
        lblimg_left.place(x=0, y=0, width=270, height=225)

        # Right frame for Double  room view
        Right_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Double Room", bg="light blue" ,fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        Right_frame.place(x=785, y=35, width=295, height=250)

        # Double room image
        img1 = Image.open(os.path.join("images", "double.png"))
        img1 = img1.resize((288, 225), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg_right1 = Label(Right_frame, image=self.photoimg1, bd=4, bg="aqua", relief=RIDGE)
        lblimg_right1.place(x=0, y=0, width=288, height=225)

        # Downframe frame for Suite room view
        Down_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Suite Room", bg="light blue" ,fg="Gray", padx=2, font=("times new roman", 12, "bold"))
        Down_frame.place(x=5, y=285, width=1075, height=245)

        # Suite room image
        img2 = Image.open(os.path.join("images", "suite.png"))
        img2 = img2.resize((493, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg_down = Label(Down_frame, image=self.photoimg2, bg="aqua",bd=4,relief=RIDGE)
        lblimg_down.place(x=0, y=0, width=493, height=220)

        img3 = Image.open(os.path.join("images", "suite1.png"))
        img3 = img3.resize((290, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg_down = Label(Down_frame, image=self.photoimg3, bd=4, bg="aqua", relief=RIDGE)
        lblimg_down.place(x=493, y=0, width=290, height=220)

        img4 = Image.open(os.path.join("images", "suite2.png"))
        img4 = img4.resize((285, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        lblimg_down = Label(Down_frame, image=self.photoimg4, bd=4, bg="aqua", relief=RIDGE)
        lblimg_down.place(x=783, y=0, width=285, height=220)
     
        

    # for show meal plan for veg. and non-veg.
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2004",
                database="management"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT day, meal_type, meal_details FROM meal_plan ORDER BY FIELD(day, 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", END, values=row)
            conn.close()
        except mysql.connector.Error as err:
            print("Error: ", err)


if __name__ == "__main__":
    root = Tk()
    app = Details_Window(root)
    root.mainloop()
