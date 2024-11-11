import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """ShellOS Houston
    Version: Beta 1.2 Linux Edition 
    (b1.2le)
    Build Number: 241110le
    Python 3.13.0
    """
    messagebox.showinfo("About ShellOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
