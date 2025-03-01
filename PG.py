from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from customer import CustWin
from details import Details_Window
from login import Login_Window
from room import RoomBooking
import os

class PGmanagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("PG Management System")
        self.root.geometry("1275x690+-5+0")


        # IMG 1
        try:
            img1 = Image.open(os.path.join("images", "PG1.png"))
            img1 = img1.resize((1280, 100), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)

            lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
            lblimg1.place(x=0, y=0, width=1280, height=100)
        except Exception as e:
            print(f"Error loading IMG 1: {e}")

        # LOGO
        try:
            img2 = Image.open(os.path.join("images", "LOGO.png"))
            img2 = img2.resize((100, 100), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
            lblimg2.place(x=0, y=0, width=100, height=100)
        except Exception as e:
            print(f"Error loading LOGO: {e}")

        # TITLE
        lbl_title = Label(self.root, text="PG MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="aqua", fg="dark gray", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=100, width=1280, height=50)

        # MAIN FRAME
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=150, width=1280, height=620)

        # MENU
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="aqua", fg="dark gray", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=200)

        # BUTTON FRAME
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=200, height=155)

        # Configure column to center-align buttons
        btn_frame.grid_columnconfigure(0, weight=1)

        # Center-aligned buttons in btn_frame
        Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="light blue", fg="gray", bd=0, cursor="hand2").grid(row=0, column=0, pady=1, sticky="ew")
        Button(btn_frame, text="ROOM", command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="light blue", fg="gray", bd=0, cursor="hand2").grid(row=1, column=0, pady=1, sticky="ew")
        Button(btn_frame, text="DETAILS", command=self.get_details, width=22, font=("times new roman", 14, "bold"), bg="light blue", fg="gray", bd=0, cursor="hand2").grid(row=2, column=0, pady=1, sticky="ew")
        Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="light blue", fg="gray", bd=0, cursor="hand2").grid(row=4, column=0, pady=1, sticky="ew")

        # RIGHT SIDE IMAGE
        try:
            right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE)
            right_frame.place(x=200, y=0, width=1075, height=540)
            img3 = Image.open(os.path.join("images", "pg3.jpg"))
            img3 = img3.resize((1075, 540), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg3 = Label(right_frame, image=self.photoimg3, bd=4, relief=RIDGE)
            lblimg3.place(x=0, y=0, width=1075, height=540)
        except Exception as e:
            print(f"Error loading right side image: {e}")

        # DOWN IMAGES
        try:
            img4 = Image.open(os.path.join("images", "PG1.png")).resize((200, 175), Image.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)
            lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
            lblimg4.place(x=0, y=190, width=200, height=175)

            img5 = Image.open(os.path.join("images", "food.jpeg")).resize((200, 180), Image.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)
            lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
            lblimg5.place(x=0, y=360, width=200, height=180)
        except Exception as e:
            print(f"Error loading down images: {e}")

    # for customers button
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.new_window.overrideredirect(True)  # Remove title bar
        self.app = CustWin(self.new_window)

    # for room details button
    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.new_window.overrideredirect(True)  # Remove title bar
        self.app = RoomBooking(self.new_window)

    # for details button
    def get_details(self):
        self.new_window = Toplevel(self.root)
        self.new_window.overrideredirect(True)  # Remove title bar
        self.app = Details_Window(self.new_window)

    # for logout, than destroy main program and open login page
    def logout(self):
        self.root.destroy()  # Close the main application window
        # Reopen the login window
        login_root = Tk()
        Login_Window(login_root)
        login_root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = PGmanagementSystem(root)
    root.mainloop()
