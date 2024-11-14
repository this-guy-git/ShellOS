import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

root = tk.Tk()
root.title("ShellOS File Manager")

folder_path = "ShellOS"  # Default folder path

def open_folder():
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=folder_path)
    listbox.delete(0, tk.END)
    for item in os.listdir(folder_path):
        listbox.insert(tk.END, item)

def open_file():
    selected_item = listbox.get(listbox.curselection())
    file_path = os.path.join(folder_path, selected_item)
    try:
        if file_path.endswith(".txt"):
            subprocess.Popen([r"notepad.exe", file_path])
        else:
            os.startfile(file_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_file():
    selected_item = listbox.get(listbox.curselection())
    file_path = os.path.join(folder_path, selected_item)
    try:
        os.remove(file_path)
        listbox.delete(listbox.curselection())
    except Exception as e:
        messagebox.showerror("Error", str(e))

def rename_file():
    selected_item = listbox.get(listbox.curselection())
    file_path = os.path.join(folder_path, selected_item)
    new_name = filedialog.asksaveasfilename(initialdir=folder_path, initialfile=selected_item)
    if new_name:
        try:
            os.rename(file_path, new_name)
            open_folder()
        except Exception as e:
            messagebox.showerror("Error", str(e))

browse_button = tk.Button(root, text="Open Folder", command=open_folder)
browse_button.pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

delete_button = tk.Button(root, text="Delete File", command=delete_file)
delete_button.pack()

rename_button = tk.Button(root, text="Rename File", command=rename_file)
rename_button.pack()

open_folder()  # Populate the listbox with the ShellOS folder's contents by default

root.mainloop()