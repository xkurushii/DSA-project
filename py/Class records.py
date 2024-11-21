import tkinter as tk
from tkinter import ttk, messagebox

# Function to create a gradient background
def create_gradient(canvas, width, height, color1, color2):
    canvas.delete("gradient")  # Clear previous gradient
    for i in range(height):
        color = "#%02x%02x%02x" % (
            int(color1[0] + (color2[0] - color1[0]) * i / height),
            int(color1[1] + (color2[1] - color1[1]) * i / height),
            int(color1[2] + (color2[2] - color1[2]) * i / height),
        )
        canvas.create_line(0, i, width, i, fill=color, tags=("gradient"))

# Convert hex color to RGB tuple
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

# Function to display the class records interface
def open_records_management():
    records_window = tk.Toplevel(root)
    records_window.title("Class Records")
    records_window.geometry("900x600")

    # Create canvas for gradient background
    records_canvas = tk.Canvas(records_window, highlightthickness=0)
    records_canvas.pack(fill="both", expand=True)

    # Gradient colors
    color1 = hex_to_rgb("#e6f7ff")
    color2 = hex_to_rgb("#005f99")

    # Apply the gradient background initially
    create_gradient(records_canvas, 900, 600, color1, color2)

    # Bind the configure event to resize the gradient when the window is resized
    records_window.bind("<Configure>", lambda event: create_gradient(records_canvas, event.width, event.height, color1, color2))

    # Header section
    header = tk.Frame(records_canvas, bg="#005f99", height=60)
    header.place(x=0, y=0, relwidth=1)
    header_label = tk.Label(header, text="CpE 114 | BSCpE 2B - Class Record", font=("Arial", 20, "bold"), bg="#005f99", fg="white")
    header_label.pack(pady=10)

    # Main button section
    button_frame = tk.Frame(records_canvas, bg="#ffffff", relief="raised", bd=2)
    button_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=250)

    # Adding buttons with additional styles and hover effects
    def on_enter(e):
        e.widget["bg"] = "#ffcc66"

    def on_leave(e):
        e.widget["bg"] = "#ffcc33"

    buttons = [
        {"text": "Midterms", "command": lambda: messagebox.showinfo("Midterms", "Midterms section opened!")},
        {"text": "Final Term", "command": lambda: messagebox.showinfo("Final Term", "Final Term section opened!")},
        {"text": "Semestral", "command": lambda: messagebox.showinfo("Semestral", "Semestral section opened!")},
    ]

    for i, btn_info in enumerate(buttons):
        btn = tk.Button(button_frame, text=btn_info["text"], font=("Arial", 16, "bold"), bg="#ffcc33", fg="black", width=15, height=2, command=btn_info["command"])
        btn.grid(row=i, column=0, pady=10)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Footer note
    footer_label = tk.Label(records_canvas, text="Data Structures and Algorithms | Academic Year 2024-2025, 1st Semester", font=("Arial", 12), bg="#ffffff", fg="#333333")
    footer_label.place(relx=0.5, rely=0.9, anchor="center")

# Function to create sections with modern buttons and icons
def create_section(parent, section_title, icon="📁", tooltip_text="Section Description"):
    section_frame = tk.Frame(parent, bg="#333333")
    section_frame.pack(fill="x", pady=5)

    # Create the button for the section
    section_button = tk.Button(
        section_frame,
        text=f"{icon}  {section_title}",
        font=("Arial", 12),
        bg="#444444",
        fg="white",
        bd=0,
        anchor="w",
        activebackground="#555555",
        activeforeground="white",
    )
    section_button.pack(fill="x", padx=10)

    # Add event bindings for tooltips
    section_button.bind("<Enter>", lambda event: show_tooltip(event, tooltip_text))
    section_button.bind("<Leave>", hide_tooltip)

    # Return the section_button to allow direct manipulation
    return section_button

# Function to show tooltip
def show_tooltip(event, text):
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{event.x_root + 20}+{event.y_root + 10}")
    label = tk.Label(tooltip, text=text, bg="lightyellow", font=("Arial", 10))
    label.pack()
    event.widget.tooltip = tooltip

def hide_tooltip(event):
    if hasattr(event.widget, 'tooltip'):
        event.widget.tooltip.destroy()

# Main window setup
root = tk.Tk()
root.title("Student Grading System")
root.geometry("900x600")

# Create canvas for gradient background
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Initial gradient color setup
color1 = hex_to_rgb("#e6f7ff")
color2 = hex_to_rgb("#005f99")

# Apply the gradient background initially
create_gradient(canvas, 900, 600, color1, color2)

# Bind the configure event to resize the gradient when the window is resized
def on_resize(event):
    create_gradient(canvas, event.width, event.height, color1, color2)

root.bind("<Configure>", on_resize)

# Create a header section
header = tk.Frame(canvas, bg="#005f99", height=60)
header.place(x=0, y=0, relwidth=1)
header_label = tk.Label(header, text="Student Grading System", font=("Arial", 20, "bold"), bg="#005f99", fg="white")
header_label.pack(pady=10)

# Create a frame for the sidebar
sidebar = tk.Frame(canvas, bg="#333333", width=250)
sidebar.place(x=0, y=60, relheight=1)

# Add the "Administrator" section at the top
admin_icon = tk.Label(sidebar, text="⚙️", font=("Arial", 30), bg="#333333", fg="white")
admin_icon.pack(pady=20)
admin_label = tk.Label(sidebar, text="ADMINISTRATOR", font=("Arial", 14, "bold"), bg="#333333", fg="white")
admin_label.pack()

# Create sections with buttons
student_management_button = create_section(sidebar, "Student Management", icon="🎓", tooltip_text="Manage student information and details.")
records_management_button = create_section(sidebar, "Records Management", icon="🗂️", tooltip_text="Manage and update student records.")
subject_management_button = create_section(sidebar, "Subject Management", icon="📚", tooltip_text="Manage subjects and course information.")

# Set command for Records Management button to open the new interface
records_management_button.config(command=open_records_management)

# Run the application
root.mainloop()
