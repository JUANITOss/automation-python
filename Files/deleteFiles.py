import os
import subprocess
from send2trash import send2trash

# Change to workspace folder (repos)
os.chdir(os.path.expanduser("~/Workspace"))

# List directories only, numbered
directories = [d for d in os.listdir() if os.path.isdir(d)]
for i, dir_name in enumerate(directories, start=1):
    print(f"{i}. {dir_name}")

# Ask the user to choose a directory by number
try:
    choice = int(input("Enter the number of the directory you want to send to the trash: "))
    if choice < 1 or choice > len(directories):
        print("Invalid choice. Exiting.")
        exit(1)
except ValueError:
    print("Please enter a valid number.")
    exit(1)

# Get the directory name based on the choice
dir_to_delete = directories[choice - 1]

# Ask for confirmation
confirmation = input(f"Are you sure you want to send '{dir_to_delete}' to the trash? Type 'yes' to confirm: ")

if confirmation.lower() == 'yes':
    # Send the directory to the trash
    send2trash(dir_to_delete)
    print(f"Directory '{dir_to_delete}' has been moved to the trash.")
else:
    print("Operation cancelled.")
