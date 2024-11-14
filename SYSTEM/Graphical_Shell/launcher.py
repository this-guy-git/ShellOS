import tkinter as tk
import subprocess

class AppLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Launcher")
        self.root.geometry("205x264")

        # Create a list of program names and their corresponding filenames
        self.programs = {
            "About Shellos": "System69/Programs/about.py",
            "Calculator": "System69/Programs/calc.py",
            "File Manager": "System69/Programs/filemgr.py",
            "Paint": "System69/Programs/paint.py",
            "Terminal": "System69/Programs/terminal.py",
            "Notepad": "System69/Programs/notepad.py",
            "Media Player": "System69/Programs/mediaplayer.py",
#           "Program": "System69/Programs/program.py",
            }

        # Create buttons for each program
        for program_name in self.programs:
            button = tk.Button(root, text=program_name, command=lambda name=program_name: self.open_program(name))
            button.pack()

    def open_program(self, program_name):
        filename = self.programs.get(program_name)
        if filename:
            try:
                # Launch the program using subprocess.Popen to avoid blocking
                subprocess.Popen(["python", filename])
                self.root.destroy()  # Close the launcher window after launching the program
            except FileNotFoundError:
                print(f"Error: {filename} not found.")
        else:
            print(f"Error: Program {program_name} not recognized.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppLauncher(root)
    root.mainloop()
