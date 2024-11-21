from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Student Grading System')
root.geometry('925x500+300+200')
root.resizable(False, False)

def switch_to_homepage():
    # Clear the screen
    for widget in root.winfo_children():
        widget.destroy()

    # Create a canvas for the gradient background
    canvas = Canvas(root, width=925, height=500)
    canvas.place(x=0, y=0)
    create_gradient(canvas, 925, 500)  # Apply gradient (blue to light blue)

    # Header for the homepage
    header = Label(root, text="Student Grading System", bg="#1f5572", fg="white",
                   font=("Arial", 20, "bold"))
    header.place(relwidth=1, height=50)

    # Sidebar for menu options
    sidebar = Frame(root, bg="#555555", width=200)
    sidebar.place(x=0, y=50, relheight=1)

    # Sidebar title
    Label(sidebar, text="ADMINISTRATOR", fg="white", bg="gray", font=("Arial", 14, "bold")).pack(pady=20)

    # Sidebar buttons with icons
    Button(sidebar, text="📋  Records", font=("Arial", 12), bg="gray", fg="white", command=show_records).pack(fill="x", pady=5)
    Button(sidebar, text="👨‍🏫  Student List", font=("Arial", 12), bg="gray", fg="white",
           command=show_student_management).pack(fill="x", pady=5)
    Button(sidebar, text="📚  Individual Report", font=("Arial", 12), bg="gray", fg="white",
           command=show_subject_management).pack(fill="x", pady=5)
    Button(sidebar, text="🚪  Logout", font=("Arial", 12), bg="gray", fg="white", command=logout).pack(fill="x", pady=5)

    # Main area background
    Label(root, bg="#c9e3f5").place(x=200, y=50, relwidth=1, relheight=1)

    # Add text to the homepage
    text = Label(root, text="CPE|114 COE2B",
                 bg="#c9e3f5", fg="#006FFC", font=("Arial", 16))
    text.place(x=240, y=75)  # Adjust placement as needed

    # Add the text for course details
    course_details = Label(root, text="Data Structure Algorithms\n2024-2025, 1st semester",
                           bg="#c9e3f5", fg="#006FFC", font=("Arial", 12))
    course_details.place(x=240, y=100)

    # Load Pangasinan State University logo
    psu_logo = PhotoImage(file=r'C:\Users\Deniss Jallorina\OneDrive\Pictures\psu.png')  # Replace with the actual path of the PSU logo image

    # Place the PSU logo beside the text
    logo_label = Label(root, image=psu_logo, bg="#c9e3f5")
    logo_label.image = psu_logo  # Keep a reference to the image to prevent garbage collection
    logo_label.place(x=430, y=70)  # Adjust position of the logo as needed

# Helper function for gradient background
def create_gradient(canvas, width, height):
    start_color = (0, 74, 153)  # Dark Blue RGB
    end_color = (102, 178, 255)  # Light Blue RGB

    for i in range(height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / height))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / height))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Placeholder functions for sidebar buttons
def show_records():
    messagebox.showinfo("Records", "Display records.")

def show_student_management():
    messagebox.showinfo("Student List", "Manage student details.")


def show_subject_management():
    messagebox.showinfo("Individual Report", "Manage subjects.")

# Return to the login screen
def logout():
    for widget in root.winfo_children():
        widget.destroy()
    create_login_screen()

def create_login_screen():
    global img, user, code, password_visible

    # Initialize password visibility state
    password_visible = False  # Initially, the password is hidden

    # Load logo image
    img = PhotoImage(file=r'C:\Users\Deniss Jallorina\OneDrive\Pictures\tester_bgg-removebg-preview.png')

    # Create gradient background for login
    canvas = Canvas(root, width=925, height=500)
    canvas.place(x=0, y=0)
    create_gradient(canvas, 925, 500)

    # Add logo image to the canvas (positioned at the right)
    canvas.create_image(250, 250, image=img)  # Adjust image position as needed

    # Login frame
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Times New Roman', 23, 'bold')).place(x=125, y=5)

    def on_enter_username(e):
        user.delete(0, 'end')

    def on_leave_username(e):
        if not user.get():
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter_username)
    user.bind('<FocusOut>', on_leave_username)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    def on_enter_password(e):
        code.delete(0, 'end')

    def on_leave_password(e):
        if not code.get():
            code.insert(0, 'Password')

    # Password entry field
    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter_password)
    code.bind('<FocusOut>', on_leave_password)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # Toggle password visibility function
    def toggle_password():
        global password_visible
        if password_visible:
            code.config(show="*")  # Hide password
        else:
            code.config(show="")  # Show password
        password_visible = not password_visible

    # Show/Hide password toggle button
    toggle_btn = Button(frame, text="👁", bg="white", bd=0, font=("Arial", 14), command=toggle_password)
    toggle_btn.place(x=295, y=150)  # Position it next to the password field

    Button(frame, width=40, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=230)

def signin():
    if user.get() == 'admin' and code.get() == 'password':
        switch_to_homepage()
    else:
        messagebox.showerror("Invalid", "Invalid username or password.")

# Start with the login screen
create_login_screen()
root.mainloop()
