import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

# Functions
def add_student():
    student_name = name_entry.get()
    student_id = id_entry.get()

    if student_name and student_id:
        tree.insert('', 'end', values=(student_name, student_id))
        name_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Both Name and Student ID are required.")

def remove_selected():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showerror("Error", "No student selected.")

def clear_all_data():
    for row in tree.get_children():
        tree.delete(row)

def toggle_theme():
    current_theme = style.theme_use()
    # Toggle between dark and light theme
    new_theme = "darkly" if current_theme != "darkly" else "flatly"
    style.theme_use(new_theme)

# Main Application
root = tk.Tk()
root.title("Student Info List")
root.geometry("1000x600")

# Modern Styling
style = Style(theme="flatly")  # Available themes: flatly, darkly, etc.
style.configure("Treeview", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial Bold", 14))

# Icons (Unicode) for buttons (simple text-based icons)
add_icon = "➕"  # Unicode plus sign
remove_icon = "❌"  # Unicode cross mark
clear_icon = "🗑️"  # Unicode trash can
theme_icon = "🌙"  # Unicode crescent moon for dark mode

# Top Bar
top_frame = tk.Frame(root, bg="blue", height=50)
top_frame.pack(side=tk.TOP, fill=tk.X)

title_label = tk.Label(top_frame, text="Student Info List", bg="blue", fg="white", font=("Arial Bold", 18))
title_label.pack(pady=10)

# Main Content Frame
main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Left Menu
menu_frame = tk.Frame(main_frame, bg="#f8f9fa", width=200)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

menu_label = tk.Label(menu_frame, text="Menu", bg="#f8f9fa", font=("Arial Bold", 14), anchor="w")
menu_label.pack(fill=tk.X, pady=10, padx=10)

# Menu Buttons (Using tk.Button instead of ttk.Button)
menu_buttons = [
    ("Add Student", add_icon, add_student),
    ("Remove Selected", remove_icon, remove_selected),
    ("Clear All Data", clear_icon, clear_all_data),
    ("Toggle Dark Mode", theme_icon, toggle_theme)
]

# Using simple Unicode characters as icons
for label, icon, command in menu_buttons:
    button = tk.Button(menu_frame, text=f"{icon}  {label}", font=("Arial", 14), command=command)
    button.pack(fill=tk.X, pady=5, padx=10)

# Right Content
right_frame = tk.Frame(main_frame, bg="white")
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# Table Section
table_frame = tk.Frame(right_frame, bg="white")
table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

columns = ("Name", "Student ID")
tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
tree.heading("Name", text="Name")
tree.heading("Student ID", text="Student ID")
tree.pack(fill=tk.BOTH, expand=True, pady=5)

# Add New Student Section
form_frame = tk.Frame(right_frame, bg="white")
form_frame.pack(fill=tk.X, pady=10)

form_label = tk.Label(form_frame, text="Add New Student", font=("Arial Bold", 14), bg="white")
form_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(form_frame, text="Name:", bg="white").grid(row=1, column=0, sticky="e", padx=5, pady=5)
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Student ID:", bg="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
id_entry = ttk.Entry(form_frame, width=30)
id_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = ttk.Button(form_frame, text="Add", command=add_student)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Footer
footer_frame = tk.Frame(right_frame, bg="white")
footer_frame.pack(fill=tk.X, pady=10)

# Run Application
root.mainloop()
