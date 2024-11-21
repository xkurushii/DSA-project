from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Global references to the entry fields (username and password) to be accessed in signin
user = None
code = None
img = None  # Global image reference for background

# Function to switch to the homepage after successful login
def switch_to_homepage():
    # Remove the login screen widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Create the homepage UI elements
    Label(root, text='Welcome to the Homepage!', bg='white', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

    # Add additional widgets for the homepage
    Button(root, text="Go to Dashboard", bg='#57a1f8', fg='white', font=('Microsoft YaHei UI Light', 12), command=show_dashboard).pack(pady=10)

    Button(root, text="Logout", bg='red', fg='white', font=('Microsoft YaHei UI Light', 12), command=logout).pack(pady=10)

# Function to show the dashboard (example of a homepage feature)
def show_dashboard():
    messagebox.showinfo("Dashboard", "Welcome to your Dashboard!")

# Function to handle logout and return to the login screen
def logout():
    # Remove the homepage widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Recreate the login screen
    create_login_screen()

# Function to create the login screen UI elements
def create_login_screen():
    global img, user, code  # To access the variables globally
    img = PhotoImage(file=r'C:\Users\Deniss Jallorina\OneDrive\Pictures\tester bgg.png')
    Label(root, image=img, bg='Sky blue').place(x=50, y=30)

    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    ##########-----------------------------------------------------

    def on_enter_username(e):
        user.delete(0, 'end')

    def on_leave_username(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter_username)
    user.bind('<FocusOut>', on_leave_username)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ##########-----------------------------------------------------

    def on_enter_password(e):
        code.delete(0, 'end')

    def on_leave_password(e):
        name = code.get()
        if name == '':
            code.insert(0, 'Password')

    # Password entry field (Initially hides the password)
    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show="*")
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter_password)
    code.bind('<FocusOut>', on_leave_password)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # Function to toggle password visibility
    def toggle_password():
        if code.cget('show') == "*":
            code.config(show="")
            toggle_btn.config(text="Hide Password")
        else:
            code.config(show="*")
            toggle_btn.config(text="Show Password")

    # Button to toggle show/hide password (placed below the password entry)
    toggle_btn = Button(frame, text="Show Password", bg='white', fg='#57a1f8', border=0, font=('Microsoft YaHei UI Light', 9), command=toggle_password)
    toggle_btn.place(x=30, y=190)  # Adjusted position to place below the password field

    ###############################################################

    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=230)
    label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
    sign_up.place(x=215, y=270)

# Function to handle sign-in logic
def signin():
    username = user.get()
    password = code.get()

    # Check if the username and password are correct
    if username == 'admin' and password == 'password':
        switch_to_homepage()
    elif username != 'admin' and password != 'password':
        messagebox.showerror("Invalid", 'Invalid username and password')
    elif password != 'password':
        messagebox.showerror("Invalid", 'Invalid password')
    elif username != 'admin':
        messagebox.showerror("Invalid", 'Invalid username')

# Start with the login screen
create_login_screen()

root.mainloop()
