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

# Main window setup
root = tk.Tk()
root.title("Test homepage haha")
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

# Create a frame for the sidebar with gradient color
sidebar = tk.Frame(canvas, bg="#333333", width=250)
sidebar.place(x=0, y=60, relheight=1)

# Add the "Administrator" section at the top
admin_icon = tk.Label(sidebar, text="⚙️", font=("Arial", 30), bg="#333333", fg="white")
admin_icon.pack(pady=20)
admin_label = tk.Label(sidebar, text="ADMINISTRATOR", font=("Arial", 14, "bold"), bg="#333333", fg="white")
admin_label.pack()

# Add tooltips for the sections
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

    # Add a click event for the button (example functionality)
    section_button.config(command=lambda: messagebox.showinfo("Info", f"You clicked on {section_title}"))

# Create sections with icons and tooltips

create_section(sidebar, "Student Management", icon="🎓", tooltip_text="Manage student information and details.")
create_section(sidebar, "Records Management", icon="🗂️", tooltip_text="Manage and update student records.")
create_section(sidebar, "Subject Management", icon="📚", tooltip_text="Manage subjects and course information.")

# Run the application
root.mainloop()
