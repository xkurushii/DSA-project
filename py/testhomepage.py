from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.resizable(False, False)

# Global references to the entry fields (username and password) to be accessed in signin
user = None
code = None
img = None  # Global image reference for background

# Function to create gradient background on canvas (sky blue to gray)
def create_gradient(canvas, width, height):
    start_color = (135, 206, 235)  # Sky Blue RGB
    end_color = (128, 128, 128)  # Gray RGB

    # Loop through the height of the canvas and create a gradient
    for i in range(height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / height))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / height))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / height))

        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color, width=1)

def switch_to_homepage():
    for widget in root.winfo_children():
        widget.destroy()

    # Create homepage header
    Label(root, text='Welcome to the School Management System', bg='white', font=('Calibri(Body)', 30, 'bold')).pack(pady=20)

    # Create buttons for navigation to different management sections
    Button(root, text="Student Management", bg='#57a1f8', fg='white', font=('Microsoft YaHei UI Light', 12),
           command=show_student_management).pack(pady=10)
    Button(root, text="Records Management", bg='#57a1f8', fg='white', font=('Microsoft YaHei UI Light', 12),
           command=show_records_management).pack(pady=10)
    Button(root, text="Subject Management", bg='#57a1f8', fg='white', font=('Microsoft YaHei UI Light', 12),
           command=show_subject_management).pack(pady=10)
    Button(root, text="Logout", bg='red', fg='white', font=('Microsoft YaHei UI Light', 12), command=logout).pack(pady=10)

def show_student_management():
    messagebox.showinfo("Student Management", "Manage student records here!")

def show_records_management():
    messagebox.showinfo("Records Management", "Manage academic and class records here!")

def show_subject_management():
    messagebox.showinfo("Subject Management", "Manage subjects and course details here!")

def logout():
    for widget in root.winfo_children():
        widget.destroy()

    create_login_screen()

def create_login_screen():
    global img, user, code
    img = PhotoImage(file=r'C:\Users\Deniss Jallorina\OneDrive\Pictures\tester_bgg-removebg-preview.png')

    # Create a canvas for background with gradient
    canvas = Canvas(root, width=925, height=500)
    canvas.place(x=0, y=0)
    create_gradient(canvas, 925, 500)  # Apply gradient (sky blue to gray)

    # Add image to the right (adjusted to x=250 to move to the right)
    canvas.create_image(250, 250, image=img)  # Moved the image to the right

    # Create the frame for the input fields (label and text entry boxes)
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Times New Roman', 23, 'bold'))
    heading.place(x=125, y=5)

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

    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show="*")
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter_password)
    code.bind('<FocusOut>', on_leave_password)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    def toggle_password():
        if code.cget('show') == "*":
            code.config(show="")
            toggle_btn.config(text="Hide Password")
        else:
            code.config(show="*")
            toggle_btn.config(text="Show Password")

    toggle_btn = Button(frame, text="Show Password", bg='white', fg='#57a1f8', border=0,
                        font=('Microsoft YaHei UI Light', 9), command=toggle_password)
    toggle_btn.place(x=30, y=190)

    ###############################################################

    Button(frame, width=40, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=230)

def signin():
    username = user.get()
    password = code.get()

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
