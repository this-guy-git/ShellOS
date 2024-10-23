import tkinter as tk
from tkinter import scrolledtext
import os
import platform
import psutil
import cpuinfo

class TerminalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal")

        # Create a scrolled text widget to simulate terminal
        self.terminal = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="black", fg="white", insertbackground="white", font=("Consolas", 12))
        self.terminal.pack(expand=True, fill=tk.BOTH)

        # Bind the Enter key to process commands
        self.terminal.bind("<Return>", self.process_command)

        # Add a prompt
        self.prompt = "/ShellOS/System69/>"
        self.terminal.insert(tk.END, self.prompt)
        self.terminal.mark_set("insert", tk.END)

    def process_command(self, event):
        # Get the current line
        line_start = self.terminal.index("insert linestart")
        line_end = self.terminal.index("insert lineend")
        line_text = self.terminal.get(line_start, line_end).strip()

        # Remove the prompt from the input to isolate the command
        if line_text.startswith(self.prompt):
            command_text = line_text[len(self.prompt):].strip()
        else:
            command_text = line_text.strip()

        # Insert a new line
        self.terminal.insert(tk.END, "\n")

        # Split the command and arguments
        parts = command_text.split()
        command = parts[0] if parts else ""
        args = parts[1:]

        # Handle commands
        if command == "exit":
            self.terminal.insert(tk.END, "Exiting...\n")
            self.root.quit()
        elif command == "help":
            self.show_help()
        elif command == "echo":
            self.terminal.insert(tk.END, " ".join(args) + "\n")
        elif command == "listdir":
            self.list_directory(args)
        elif command == "about":
            self.show_about()
        elif command == "run":
            self.run_file(args)
        elif command == "sysfetch":
            self.sysfetch()
        else:
            self.terminal.insert(tk.END, f"Command not found: {command_text}\n")
        
        # Add a new prompt
        self.terminal.insert(tk.END, self.prompt)
        self.terminal.mark_set("insert", tk.END)
        self.terminal.see(tk.END)

        # Prevent default newline behavior
        return "break"

    def show_help(self):
        help_text = (
            "Available commands:\n"
            "help      - Displays this help message\n"
            "echo      - Echoes the input text\n"
            "listdir   - Lists all files and directories in the specified directory (defaults to the current directory)\n"
            "about     - Displays information about ShellOS\n"
            "exit      - Exits the terminal\n"
            "run       - Executes the specified .py file\n"
            "sysfetch   - Displays system information\n"
        )
        self.terminal.insert(tk.END, help_text + "\n")

    def list_directory(self, args):
        if args:
            directory = args[0]
        else:
            directory = os.getcwd()
        
        try:
            items = os.listdir(directory)
            for item in items:
                self.terminal.insert(tk.END, item + "\n")
        except FileNotFoundError:
            self.terminal.insert(tk.END, f"Error: Directory '{directory}' not found.\n")

    def show_about(self):
        about_text = (
            "ShellOS Version: Beta 1.2 (b1.2)\n"
            "Build Number: 241023\n"
            "Core Version: 1.0\n"
            f"Ram: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB\n"
            f"CPU: {platform.processor()}\n"
        )
        self.terminal.insert(tk.END, about_text + "\n")

    def sysfetch(self):
        self.terminal.insert(tk.END, "===== ShellOS Information =====\n")

        # Display ShellOS Information
        self.terminal.insert(tk.END, f"Name: ShellOS Dallas\n")
        self.terminal.insert(tk.END, f"Version: Beta 1.2\n")
        self.terminal.insert(tk.END, f"Build Number: 241023\n")

        # Display CPU Information
        self.terminal.insert(tk.END, "\n===== CPU Information =====\n")
        cpu_info = cpuinfo.get_cpu_info()
        self.terminal.insert(tk.END, f"Processor Name: {cpu_info['brand_raw']}\n")
        self.terminal.insert(tk.END, f"Physical Cores: {psutil.cpu_count(logical=False)}\n")
        self.terminal.insert(tk.END, f"Total Cores: {psutil.cpu_count(logical=True)}\n")

        # Display Memory Information
        svmem = psutil.virtual_memory()
        self.terminal.insert(tk.END, "\n===== Memory Information =====\n")
        self.terminal.insert(tk.END, f"Total RAM: {svmem.total / (1024 ** 3):.2f} GB\n")
        self.terminal.insert(tk.END, f"Available RAM: {svmem.available / (1024 ** 3):.2f} GB\n")
        self.terminal.insert(tk.END, f"Used RAM: {svmem.used / (1024 ** 3):.2f} GB\n")
        self.terminal.insert(tk.END, f"RAM Usage: {svmem.percent}%\n")

        # Display Storage Information
        self.terminal.insert(tk.END, "\n===== Storage Information =====\n")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                self.terminal.insert(tk.END, f"\nDevice: {partition.device}\n")
                self.terminal.insert(tk.END, f"  Mount Point: {partition.mountpoint}\n")
                self.terminal.insert(tk.END, f"  File System Type: {partition.fstype}\n")
                self.terminal.insert(tk.END, f"  Total Size: {usage.total / (1024 ** 3):.2f} GB\n")
                self.terminal.insert(tk.END, f"  Used Size: {usage.used / (1024 ** 3):.2f} GB\n")
                self.terminal.insert(tk.END, f"  Free Size: {usage.free / (1024 ** 3):.2f} GB\n")
                self.terminal.insert(tk.END, f"  Usage: {usage.percent}%\n")
            except PermissionError:
                self.terminal.insert(tk.END, f"Skipping {partition.device} as it is not ready.\n")

    def run_file(self, args):
        if not args:
            self.terminal.insert(tk.END, "Error: No file specified.\n")
            return
        
        file_to_run = args[0]
        
        if not file_to_run.lower().endswith(".py"):
            file_to_run += ".py"

        if os.path.isabs(file_to_run):
            file_path = file_to_run
        else:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_directory, file_to_run)

        print(f"Attempting to run file: {file_path}")

        if not os.path.isfile(file_path):
            self.terminal.insert(tk.END, f"Error: File '{file_path}' not found.\n")
            return
        
        try:
            result = subprocess.run(["python", file_path], capture_output=True, text=True)
            self.terminal.insert(tk.END, result.stdout)
            if result.stderr:
                self.terminal.insert(tk.END, result.stderr)
        except Exception as e:
            self.terminal.insert(tk.END, f"Error: {str(e)}\n")

root = tk.Tk()
app = TerminalApp(root)
root.geometry("800x600")
root.mainloop()
