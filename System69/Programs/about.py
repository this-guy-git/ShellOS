import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """ShellOS 
    Version:1.0
    Python 3.12.6
    Pip 24.2
    """
    messagebox.showinfo("About ShellOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
