import tkinter as tk

def change_color():
    selected_color = color_var.get()
    root.config(bg=selected_color)

root = tk.Tk()
root.title("Color Picker")

# List of colors
colors = ["Red", "Green", "Blue", "Yellow"]

# Variable to store selected color
color_var = tk.StringVar(root)
color_var.set(colors[1])  # Set default value

# Dropdown menu to select color
color_menu = tk.OptionMenu(root, color_var, *colors)
color_menu.pack(pady=10)

# Button to change background color
change_button = tk.Button(root, text="Change Color", command=change_color)
change_button.pack(pady=5)

root.mainloop()
