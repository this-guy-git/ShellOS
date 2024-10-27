import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """ShellOS 
    Version: Beta 1.3-Pre 
    Build Number: 241026
    Python 3.12.6
    """
    messagebox.showinfo("About ShellOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
