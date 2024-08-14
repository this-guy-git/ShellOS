import tkinter as tk
import subprocess
import os
from datetime import datetime

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
        self.clock_label = tk.Label(self.taskbar, text="00:00 January 1, 2000", bg="gray")
        self.clock_label.pack(side="right", padx=10, pady=2)

        # Start the clock
        self.update_clock()

        # Fullscreen state
        self.fullscreen = False

        # Bind F11 to toggle fullscreen
        self.root.bind("<F11>", self.toggle_fullscreen)

    def open_launcher(self):
        # Path to the launcher script
        launcher_script = os.path.join(os.getcwd(), 'System69', 'Launcher.py')
        
        # Open the launcher script using subprocess
        subprocess.Popen(['python', launcher_script])

    def update_clock(self):
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M %B %d, %Y")
        except:
            # Default to 00:00 January 1, 2000 if system time can't be detected
            current_time = "00:00 January 1, 2000"
        
        self.clock_label.config(text=current_time)
        
        # Update the clock every second (1000 milliseconds)
        self.root.after(1000, self.update_clock)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = ShellOS(root)
    root.mainloop()
