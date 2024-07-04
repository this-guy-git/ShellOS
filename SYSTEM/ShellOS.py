import tkinter as tk
import subprocess
import os

class ShellOS:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellOS")
        
        # Set the size of the window
        self.root.geometry("800x600")
        
        # Create a taskbar
        self.taskbar = tk.Frame(root, bg="gray", height=30)
        self.taskbar.pack(side="top", fill="x")
        
        # Create a launcher button
        self.launcher_button = tk.Button(self.taskbar, text="Launcher", command=self.open_launcher)
        self.launcher_button.pack(side="left", padx=5, pady=2)
        
        # Create a demo clock label
        self.clock_label = tk.Label(self.taskbar, text="00:00", bg="gray")
        self.clock_label.pack(side="right", padx=10, pady=2)
        
    def open_launcher(self):
        # Path to the launcher script
        launcher_script = os.path.join(os.getcwd(), 'System69', 'Launcher.py')
        
        # Open the launcher script using subprocess
        subprocess.Popen(['python', launcher_script])

if __name__ == "__main__":
    root = tk.Tk()
    app = ShellOS(root)
    root.mainloop()
