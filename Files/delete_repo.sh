#!/bin/bash

# Function to check if send2trash is installed
check_send2trash_installed() {
    python3 -c "import send2trash" 2>/dev/null
}

# Function to install send2trash if not installed
install_send2trash() {
    echo "send2trash module not found. Installing..."
    sudo apt update
    sudo apt install -y python3-send2trash
}

# Check if send2trash is installed, install if necessary
if ! check_send2trash_installed; then
    install_send2trash
else
    echo "send2trash module is already installed."
fi

# Run the Python script
python3 <<EOF
import os
from send2trash import send2trash

os.chdir(os.path.expanduser("~/Workspace"))

directories = [d for d in os.listdir() if os.path.isdir(d)]
for i, dir_name in enumerate(directories, start=1):
    print(f"{i}. {dir_name}")

try:
    choice = int(input("Enter the number of the directory you want to send to the trash: "))
    if choice < 1 or choice > len(directories):
        print("Invalid choice. Exiting.")
        exit(1)
except ValueError:
    print("Please enter a valid number.")
    exit(1)

dir_to_delete = directories[choice - 1]

confirmation = input(f"Are you sure you want to send '{dir_to_delete}' to the trash? Type 'yes' to confirm: ")

if confirmation.lower() == 'yes':
    send2trash(dir_to_delete)
    print(f"Directory '{dir_to_delete}' has been moved to the trash.")
else:
    print("Operation cancelled.")
EOF
