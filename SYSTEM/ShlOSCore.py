# ShellOS Version: beta 1.1
# Core Version: 1.0

import os

# Get the directory where ShlOSCore.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Since ShellOS.py is in the same directory, just reference it directly
GUI = os.path.join(script_dir, "ShlOSShell.py")

# Check if the ShellOS script exists
if os.path.exists(GUI):
    os.system(f'python "{GUI}"')
else:
    print(f"Error: {GUI} not found.")
