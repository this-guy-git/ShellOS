import subprocess
import os
import time
import sys
import psutil
import platform

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

def verify_hardware():
    print("Verifying your hardware...")
    
    # Get CPU info
    cpu_name = platform.processor()
    cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else 0
    cpu_cores = psutil.cpu_count(logical=False)
    
    # Get RAM info
    ram_total = psutil.virtual_memory().total / (1024 ** 2)  # Convert to MB
    
    # Get primary storage info
    storage_info = psutil.disk_usage('/')
    storage_free = storage_info.free / (1024 ** 2)  # Convert to MB
    
    # Display hardware details
    print("\nDetected Hardware:")
    print(f"CPU: {cpu_name}")
    print(f"CPU Frequency: {cpu_freq:.2f} MHz")
    print(f"CPU Cores: {cpu_cores}")
    print(f"Total RAM: {ram_total:.2f} MB")
    print(f"Free Storage on Primary Device: {storage_free:.2f} MB\n")
    
    # Verify hardware requirements
    if cpu_freq < 250:
        print("Error: CPU frequency must be at least 250 MHz.")
        sys.exit(1)
    if cpu_cores < 1:
        print("Error: CPU must have at least 1 core.")
        sys.exit(1)
    if ram_total < 192:
        print("Error: System RAM must be at least 192 MB.")
        sys.exit(1)
    if storage_free < 25:
        print("Error: Free storage must be at least 25 MB.")
        sys.exit(1)
    
    print("Hardware requirements met.\n")

def main():
    print(r"""
                             ▒▒▒▒▒▒▒▒▒                             
                       ▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒                       
                   ▒▒▒▒▒▓██▓▓▒▓▓▓▒▓▓▓▓▓████▓▒▒▒▒                   
                ▒▒▒▒▒▓█▓▓▓▓█▓▓█▓▓█▓▓▒▓▓█▓▒▒▒▒▒▒▒▒▒▒                
              ▒▒▒▒▓█▓▒▓█▓▓█▓█▓▒░░▒░▒▒▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒              
             ▒▒▒▒▓▓▓▓▓█▓▓█▓▓▓▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓█▒▒▒▒▒            
           ▒▒▒▒▒▓▓▒▓▓▓█▒█▓▒▒▒▒▒▒░▒▒▓▒░▒▒▒▒▒▒▒▓█▓▒▓█▒▒▒▒▒           
          ▒▒▒▒▒▓▓▓▓▓▒▓▓▒▒▒▓▓▓▓▓▓▒▓▓▓▓▒░▒▒▒▓█▓▓▓▓▒▓▓▓▒▓▓▒▒          
         ▒▒▒▓▓▓▓▓▓▒▓▓▓▒▒▓▓▓▓▒▒▓█████▓▒░▓█▓▓▒▓█▓▒▓█▓▓▓▒▒▒▒▒         
         ▒▒▒▓▓▓▓▒▓▒▓▓▒▒▓▓▓▓▒▒▒▓██▓▓▓▒▒▒▒▒█▓▓██▓▒██▓▓▓▒▒▒▒▒▒        
        ▒▒▒▒▓█▓▓▒▒▓▒▒▓▓▓▓▓▓▓▒▓█▓▓████▓▒▒▒▓▓▓█▓▒▓█▓▒▓▓▒▒▓▒▒▒        
        ▒▒▒▓▓██▓▒▒▒▒▓▓▓▓▒▒▒▒██████████▒▒░▒▒▓▓▒▓█▓▓▓▓▓▒▓▓▒▒▒        
        ▒▒▒▓▒▓██▓▒▒▒▒▒▓▓▓▒▒▓███████████▒▒▒░▒▒▓▓▓▓▓▓▓▓▒▓▓▓▒▒▒       
        ▒▒▒▓▒▓▓██▓▒▒▒▒▒▒▒▒▓█████████████▒▒▒▒▒▓▓▓▓▓▒▓▓▒▓▓▒▒▒▒       
        ▒▒▒▓▓▒▓▓▓█▓▒▒▒▒▒▒▒██████████████▓▒▒▒▒▒▓▓▒▓▓▓▒▓█▓▒▒▒        
        ▒▒▒▓▓▒▒▓▓▓██▓▒▒▒▒▓███████████████▒▒▒░▒▒▓▓▒▓▒▓█▓▓▒▒▒        
         ▒▒▒▓▓▒▒▓▓▓▓██▓▓▒▓██████████████▓▒▒▒▒▒▓▒▓▓▒▓█▓▓▒▒▒▒        
         ▒▒▒▒▓▓▓▒▒▓▓▓▓███▓▒▓███████████▓▓▒▒▒▒█▓▓▒▓█▓▓▓▒▒▒▒         
          ▒▒▒▒▓▓▓▒▓▓██████▓▒▒▓█████████▓█▓▓▓█████▓▓▓▒▒▒▒▒          
           ▒▒▒▒▒▓▓▓▓████████▓████████▒▒▓███████▓▓▓▒▒▒▒▒▒           
             ▒▒▒▒▓▓▓▓███████▓▒▒▒▓▒▒▒░▒▒▓███▓▓▓▓▓▒▒▒▒▒▒▒            
              ▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒              
                ▒▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
                   ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒                  
                       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                       
                              ▒▒▒▒▒▒▒                                                         
""")

    print(r"""
                 ____  _          _ _  ___  ____  
                / ___|| |__   ___| | |/ _ \/ ___|   
                \___ \| '_ \ / _ \ | | | | \___ \ 
                 ___) | | | |  __/ | | |_| |___) |
                |____/|_| |_|\___|_|_|\___/|____/  

                    _      _                  
                   | |    (_)                 
                   | |     _ _ __  _   ___  __
                   | |    | | '_ \| | | \ \/ /
                   | |____| | | | | |_| |>  < 
                   |______|_|_| |_|\__,_/_/\_\
""")

    print("Starting ShellOS Beta 1.0")
    time.sleep(2)  # Delay for 2 seconds to simulate loading time

    # Verify hardware requirements
    verify_hardware()

    # Install required packages
    install_requirements()

    # Path to the ShellOS script
    shellos_script = os.path.join(os.getcwd(), 'SYSTEM/ShlOSCore.py')

    # Run the ShellOS script
    subprocess.Popen(['python', shellos_script])

if __name__ == "__main__":
    main()
