import subprocess
import os
import time
import sys

def install_requirements():
    """Installs required packages from requirements.txt."""
    requirements_file = os.path.join(os.getcwd(), 'requirements.txt')
    if os.path.isfile(requirements_file):
        try:
            print("Installing required packages...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
            print("All required packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install required packages: {e}")
            sys.exit(1)
    else:
        print("requirements.txt file not found.")
        sys.exit(1)

def main():
    print("Starting ShellOS...")
    time.sleep(2)  # Delay for 2 seconds to simulate loading time

    # Install required packages
    install_requirements()

    # Path to the ShellOS script
    shellos_script = os.path.join(os.getcwd(), 'SYSTEM/ShellOS.py')

    # Run the ShellOS script
    subprocess.Popen(['python', shellos_script])

if __name__ == "__main__":
    main()
