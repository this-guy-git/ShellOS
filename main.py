import subprocess
import os
import time

def main():
    print("Starting ShellOS...")
    time.sleep(2)  # Delay for 2 seconds to simulate loading time

    # Path to the ShellOS script
    shellos_script = os.path.join(os.getcwd(), 'SYSTEM/ShellOS.py')

    # Run the ShellOS script
    subprocess.Popen(['python', shellos_script])

if __name__ == "__main__":
    main()
