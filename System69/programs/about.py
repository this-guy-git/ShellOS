import tkinter as tk
from tkinter import messagebox

def about_program():
    info = """ShellOS Dallas
    Version: Beta 1.2 (b1.2)
    Build Number: 241023
    Python 3.12.6
    """
    messagebox.showinfo("About ShellOS", info)

def main():
    about_program()

if __name__ == "__main__":
    main()
