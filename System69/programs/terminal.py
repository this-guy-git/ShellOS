import sys
import os
import subprocess 
# ShellOS Version
VERSION = "Alpha 0.45"

def help_command():
    return "Available commands: help, greet, exit, sysinfo, run, del, pkg"

def exit_command():
    print("Exiting...")
    sys.exit()

def sysinfo_command():
    return f"ShellOS Version: {VERSION}\n thonga you should add some stuff here."

def run_command(file):
    if os.path.isfile(file):
        try:
            with open(file) as f:
                code = f.read()
            exec(code, globals(), {})
            return f"Executed {file} successfully."
        except Exception as e:
            return f"Failed to execute {file}: {str(e)}"
    else:
        return f"No such file: {file}"

def del_command(file):
    if os.path.isfile(file):
        try:
            os.remove(file)
            return f"Deleted {file} successfully."
        except Exception as e:
            return f"Failed to delete {file}: {str(e)}"
    else:
        return f"No such file: {file}"


def pkg_command(action, package):
    if action == "install":
        try:
            result = subprocess.run(["sudo", "apt-get", "install", "-y", package], check=True, text=True, capture_output=True)
            return f"Installed package: {package} successfully.\n{result.stdout}"
        except subprocess.CalledProcessError as e:
            return f"Failed to install package: {package}. Error: {e.stderr}"
    else:
        return f"Unknown subcommand '{action}' for pkg. Use 'install'."


def unknown_command():
    return "Unknown command. Try the 'help' command."

# Mapping commands to their functions
commands = {
    'help': help_command,
    'greet': greet_command,
    'exit': exit_command,
    'sysinfo': sysinfo_command,
    'run': run_command,
    'del': del_command,
    'pkg': pkg_command
}

def main():
    print("Welcome to the custom terminal. Type 'help' to see the list of commands.")
    while True:
        try:
            user_input = input("> ").strip().split()
            if not user_input:
                continue

            command = user_input[0]
            args = user_input[1:]

            if command in commands:
                if args:
                    try:
                        result = commands[command](*args)
                    except TypeError as e:
                        result = f"Invalid arguments. Error: {str(e)}"
                else:
                    result = commands[command]()
            else:
                result = unknown_command()

            print(result)
        except Exception as e:
            print(f"An error occurred: {str(e)}")



if __name__ == "__main__":
    main()