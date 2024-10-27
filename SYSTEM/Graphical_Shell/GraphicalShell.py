import tkinter as tk
import subprocess
import os
from datetime import datetime
from PIL import Image, ImageTk  # Importing Image and ImageTk from PIL

class ShellOS:
    def __init__(self, root):
        self.root = root
        self.root.title("ShellOS Beta 1.3-Pre Release")

        # Set custom icon for title bar and taskbar
        icon_path = "SYSTEM/Graphical_Shell/icons/shellos.png"  # Replace with your actual icon file path
        self.root.iconphoto(False, tk.PhotoImage(file=icon_path))

        self.root.geometry("1017x660")
        self.root.minsize(1017, 660)
        self.root.maxsize(1017, 660)
        self.root.resizable(False, False)  # Disable window resizing in both directions

        # Create the taskbar and place it at the top
        self.taskbar = tk.Frame(root, bg="gray", height=30)
        self.taskbar.place(x=0, y=0, relwidth=1, height=30)

        self.launcher_button = tk.Button(self.taskbar, text="Launcher", command=self.open_launcher)
        self.launcher_button.pack(side="left", padx=5, pady=2)

        self.clock_label = tk.Label(self.taskbar, text="00:00 January 1, 2000", bg="gray")
        self.clock_label.pack(side="right", padx=10, pady=2)

        self.update_clock()

        # Create a label for the wallpaper
        self.wallpaper = tk.Label(root)
        self.wallpaper.place(x=0, y=30, width=1017, height=630)  # Adjust height to avoid overlap

        # Load the image using Pillow
        self.bg_image = Image.open("SYSTEM/Graphical_Shell/wallpaper.png")  # Change to your image file
        self.bg_image = self.bg_image.resize((1017, 630), Image.LANCZOS)  # Resize to fit the window
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)  # Convert to PhotoImage

        self.wallpaper.config(image=self.bg_image_tk)

        self.fullscreen = False

        self.root.bind("<F11>", self.toggle_fullscreen)

        self.version_label = tk.Label(root, text="ShellOS Beta 1.3-Pre Build 241026", anchor="se")
        self.version_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-5)

    def open_launcher(self):
        launcher_script = os.path.join(os.getcwd(),'SYSTEM', 'Graphical_Shell', 'Launcher.py')
        
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
