import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """ShellOS Beta
    Version 1.1
    Python 3.12.3
    """
    messagebox.showinfo("About ShellOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
