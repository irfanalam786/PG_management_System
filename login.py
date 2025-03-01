import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import re
import os

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1270x690+-8+0")

        # Variables
        self.var_username = StringVar()
        self.var_password = StringVar()

        # Background Image
        try:
            self.bg = ImageTk.PhotoImage(file=os.path.join("images", "Background.jpg"))
            lbl_bg = Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")

        # Login Frame
        frame_width = 340
        frame_height = 450

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates for centering
        x_coordinate = (screen_width // 2) - (frame_width // 2)
        y_coordinate = (screen_height // 2) - (frame_height // 2)

        # Place the frame at the calculated position
        frame = Frame(self.root, bg="white")
        frame.place(x=x_coordinate, y=y_coordinate, width=frame_width, height=frame_height)


        # User Icon
        try:
            img1 = Image.open(os.path.join("images", "user.jpg"))
            img1 = img1.resize((100, 100), Image.LANCZOS)
            self.photoimage1 = ImageTk.PhotoImage(img1)
            lblimg1 = Label(frame, image=self.photoimage1, bg="white", borderwidth=0)
            lblimg1.place(x=120, y=5, width=100, height=100)
        except Exception as e:
            print(f"Error loading user icon: {e}")

        # Username and Password Fields
        get_str = Label(frame, text="Get Started", font=("times new roman", 15, "bold"), bg="white", fg="Grey")
        get_str.place(x=115, y=105)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="Grey")
        username.place(x=40, y=165)
        self.txtuser = ttk.Entry(frame, textvariable=self.var_username, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=195, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="Grey")
        password.place(x=40, y=235)
        self.txtpassword = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"), show="*")
        self.txtpassword.place(x=40, y=265, width=270)

        # Login Button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="Grey", activebackground="red")
        loginbtn.place(x=110, y=310, width=120, height=40)

        # New User Register Button
        registerbtn = Button(frame, text="New User Register", command=self.new_user_register, font=("times new roman", 15, "bold"), borderwidth=0, fg="Grey", bg="white", activeforeground="Grey", activebackground="white")
        registerbtn.place(x=10, y=360, width=200, height=35)

        # Forgot Password Button
        forgotbtn = Button(frame, text="Forgot Password", command=self.forgot_password, font=("times new roman", 15, "bold"), borderwidth=0, fg="Grey", bg="white", activeforeground="Grey", activebackground="white")
        forgotbtn.place(x=20, y=400, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            # Check if user exists in the database (MySQL)
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2004",
                database="management"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpassword.get()))
            user = cursor.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Successful", "Welcome to PG MANAGEMENT SYSTEM")
                self.open_management()  # Open PG management system in a new window
            else:
                messagebox.showerror("Invalid", "Invalid username or password")

    def open_management(self):
        self.root.destroy()
        from PG import PGmanagementSystem
        management_window = Tk()  # Create a new root window for the management system
        app = PGmanagementSystem(management_window)
        management_window.mainloop()

    def new_user_register(self):
        # New Registration Window
        self.new_register_window = Toplevel(self.root, bg="white")
        self.new_register_window.title("New User Registration")
        self.new_register_window.overrideredirect(True)

        # Set the dimensions of the window
        window_width = 340
        window_height = 480

        # Get screen width and height
        screen_width = self.new_register_window.winfo_screenwidth()
        screen_height = self.new_register_window.winfo_screenheight()

        # Calculate x and y coordinates for centering
        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)

        # Set the geometry of the window
        self.new_register_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Registration Fields
        Label(self.new_register_window, text="New User Registration", font=("times new roman", 20, "bold")).pack(pady=20)

        Label(self.new_register_window, text="Email", font=("times new roman", 12)).pack(pady=2)
        email_entry = ttk.Entry(self.new_register_window, font=("times new roman", 12))
        email_entry.pack(pady=2)

        Label(self.new_register_window, text="Password", font=("times new roman", 12)).pack(pady=2)
        password_entry = ttk.Entry(self.new_register_window, font=("times new roman", 12), show="*")
        password_entry.pack(pady=2)

        Label(self.new_register_window, text="Confirm Password", font=("times new roman", 12)).pack(pady=2)
        confirm_password_entry = ttk.Entry(self.new_register_window, font=("times new roman", 12), show="*")
        confirm_password_entry.pack(pady=2)

        Label(self.new_register_window, text="Security Question", font=("times new roman", 12)).pack(pady=2)
        security_question_combo = ttk.Combobox(self.new_register_window, values=["What is your pet's name?", "enter your mother's maiden name? your mother's maiden name?", "enter your first school?"], font=("times new roman", 12), state="readonly")
        security_question_combo.pack(pady=2)

        Label(self.new_register_window, text="Answer", font=("times new roman", 12)).pack(pady=2)
        answer_entry = ttk.Entry(self.new_register_window, font=("times new roman", 12))
        answer_entry.pack(pady=2)

        # Register Button
        def register_user():
            email = email_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
            security_question = security_question_combo.get()
            answer = answer_entry.get()

            # Check if any field is empty
            if not email or not password or not confirm_password or not security_question or not answer:
                messagebox.showerror("Error", "All fields are required")
                return

            # Check if the email contains '@'
            if "@" not in email:
                messagebox.showerror("Error", "Invalid email address. It must contain '@'.")
                return

            # Validate passwords match
            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return

            # Store user in the MySQL database
            self.store_user(email, password, security_question, answer)

            messagebox.showinfo("Success", "Registration Successful!", parent=self.root)
            self.new_register_window.destroy()

        register_button = Button(self.new_register_window, text="Register", fg="white", bg="red", command=register_user, font=("times new roman", 15, "bold"))
        register_button.pack(pady=20)


    def forgot_password(self):
        # Forgot Password Window
        self.forgot_window = Toplevel(self.root, bg="white")
        self.forgot_window.title("Forgot Password")
        self.forgot_window.overrideredirect(True)

        # Set the dimensions of the window
        window_width = 340
        window_height = 480

        # Get screen width and height
        screen_width = self.forgot_window.winfo_screenwidth()
        screen_height = self.forgot_window.winfo_screenheight()

        # Calculate x and y coordinates for centering
        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)

        # Set the geometry of the window
        self.forgot_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Username Field
        Label(self.forgot_window, text="Enter Username (Email)", font=("times new roman", 12)).pack(pady=10)
        username_entry = ttk.Entry(self.forgot_window, font=("times new roman", 12))
        username_entry.pack(pady=2)

        # Security Question Field
        Label(self.forgot_window, text="Select Security Question", font=("times new roman", 12)).pack(pady=10)
        security_question_combo = ttk.Combobox(self.forgot_window, values=["What is your pet's name?", "enter your mother's maiden name?", "enter your first school?"], font=("times new roman", 12), state="readonly")
        security_question_combo.pack(pady=2)

        # Answer Field
        Label(self.forgot_window, text="Answer", font=("times new roman", 12)).pack(pady=10)
        answer_entry = ttk.Entry(self.forgot_window, font=("times new roman", 12))
        answer_entry.pack(pady=2)

        # New Password Fields
        Label(self.forgot_window, text="New Password", font=("times new roman", 12)).pack(pady=10)
        new_password_entry = ttk.Entry(self.forgot_window, font=("times new roman", 12), show="*")
        new_password_entry.pack(pady=2)

        Label(self.forgot_window, text="Confirm New Password", font=("times new roman", 12)).pack(pady=10)
        confirm_new_password_entry = ttk.Entry(self.forgot_window, font=("times new roman", 12), show="*")
        confirm_new_password_entry.pack(pady=2)

        # Reset Password Button
        def reset_password():
            username = username_entry.get()
            security_question = security_question_combo.get()
            answer = answer_entry.get()
            new_password = new_password_entry.get()
            confirm_new_password = confirm_new_password_entry.get()

            # Check if all fields are filled
            if not username or not security_question or not answer or not new_password or not confirm_new_password:
                messagebox.showerror("Error", "All fields are required", parent=self.root)
                return

            # Validate email format (contains '@')
            if '@' not in username or '.' not in username:
                messagebox.showerror("Error", "Invalid email format. Please include '@' symbol.", parent=self.root)
                return

            # Check if the username exists in the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2004",
                database="management"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s", (username,))
            user = cursor.fetchone()

            if user:
                # Validate the security question and answer
                if user[3] == security_question and user[4] == answer:
                    if new_password == confirm_new_password:
                        # Update password in the database
                        cursor.execute("UPDATE users SET password=%s WHERE email=%s", (new_password, username))
                        conn.commit()
                        messagebox.showinfo("Success", "Password reset successful!", parent=self.root)
                        self.forgot_window.destroy()
                    else:
                        messagebox.showerror("Error", "Passwords do not match", parent=self.root)
                else:
                    messagebox.showerror("Error", "Security question or answer is incorrect", parent=self.root)
            else:
                messagebox.showerror("Error", "Username not found", parent=self.root)
            conn.close()

        reset_button = Button(self.forgot_window, text="Reset Password", fg="white", bg="red", command=reset_password, font=("times new roman", 15, "bold"))
        reset_button.pack(pady=20)

    def store_user(self, email, password, security_question, answer):
        try:
            # Establish MySQL connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2004",
                database="management"
            )
            cursor = conn.cursor()
            
            # Insert user data into the 'users' table
            query = "INSERT INTO users (email, password, security_question, answer) VALUES (%s, %s, %s, %s)"
            values = (email, password, security_question, answer)
            cursor.execute(query, values)
            
            # Commit and close connection
            conn.commit()
            conn.close()
            print("User registered successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            messagebox.showerror("Error", "Could not store user data",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
