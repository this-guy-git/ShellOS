import tkinter as tk
import subprocess
import os
from datetime import datetime

class ShellOS:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellOS Beta 1.2")

        self.root.geometry("1017x660")

        self.taskbar = tk.Frame(root, bg="gray", height=30)
        self.taskbar.pack(side="top", fill="x")

        self.launcher_button = tk.Button(self.taskbar, text="Launcher", command=self.open_launcher)
        self.launcher_button.pack(side="left", padx=5, pady=2)

        self.clock_label = tk.Label(self.taskbar, text="00:00 January 1, 2000", bg="gray")
        self.clock_label.pack(side="right", padx=10, pady=2)

        self.update_clock()

        self.fullscreen = False

        self.root.bind("<F11>", self.toggle_fullscreen)

        self.version_label = tk.Label(root, text="ShellOS Beta 1.2 Build 241023", anchor="se")
        self.version_label.pack(side="bottom", anchor="se", padx=10, pady=5)

    def open_launcher(self):
        launcher_script = os.path.join(os.getcwd(), 'System69', 'Launcher.py')
        
        subprocess.Popen(['python', launcher_script])

    def update_clock(self):
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M %B %d, %Y")
        except:
            current_time = "00:00 January 1, 2000"
        
        self.clock_label.config(text=current_time)

        self.root.after(1000, self.update_clock)

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = ShellOS(root)
    root.mainloop()
