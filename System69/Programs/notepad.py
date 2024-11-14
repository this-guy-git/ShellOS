import os
import tkinter as tk
from tkinter import filedialog, Text

def view_file():
    file_path = filedialog.askopenfilename(initialdir="System69/Documents", title="Select a File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)
    except FileNotFoundError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "File not found.")

def create_file():
    file_path = filedialog.asksaveasfilename(initialdir="System69/Documents", title="Save File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    content = text.get(1.0, tk.END)
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            status_label.config(text=f"File '{os.path.basename(file_path)}' created and saved to System69/Documents")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("ShellOS Notepad")

# Create the text area for displaying file contents
text = Text(root, height=10, width=50)
text.pack()

# Create buttons for viewing and creating files
view_button = tk.Button(root, text="View File", command=view_file)
view_button.pack()
create_button = tk.Button(root, text="Create File", command=create_file)
create_button.pack()

# Create a label for status messages
status_label = tk.Label(root, text="")
status_label.pack()

# Run the main loop
root.mainloop()