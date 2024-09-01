# Importing the pathlib module for path manipulations
from pathlib import Path

# Handling file and directory paths using pathlib

# Joining paths
# Using '/' operator to join paths
path = Path('usr') / 'bin' / 'spam'
print(path)  # Output: usr/bin/spam

# Creating new folders
# The mkdir() method is used to create directories
# 'parents=True' allows creation of intermediate directories
path = Path.cwd() / 'delicious' / 'walnut' / 'waffles'
path.mkdir(parents=True)

# Checking if a path is absolute or relative
# is_absolute() checks if a path is absolute
print(Path('/').is_absolute())  # Output: True
print(Path('..').is_absolute())  # Output: False

# Extracting an absolute path
# resolve() returns the absolute path
print(Path('..').resolve())  # Output: /home (example)

# Handling relative paths
# relative_to() gets the relative path from a base path
print(Path('/etc/passwd').relative_to('/'))  # Output: etc/passwd

# Checking if a file/directory exists
# exists() checks if the path exists
print(Path('.').exists())  # Output: True
print(Path('setup.py').exists())  # Output: True
print(Path('nonexistentfile').exists())  # Output: False

# Checking if a path is a file or directory
# is_file() and is_dir() check if the path is a file or directory respectively
print(Path('setup.py').is_file())  # Output: True
print(Path('/home').is_file())  # Output: False
print(Path('/').is_dir())  # Output: True
print(Path('setup.py').is_dir())  # Output: False

# Getting a file's size in bytes
# stat() returns file statistics including size
stat = Path('/bin/python3.6').stat()
print(stat.st_size)  # Output: 10024 (example)

# Listing directory contents
# iterdir() lists files and directories in the given path
for f in Path('/usr/bin').iterdir():
    print(f)

# Getting directory file sizes
# Calculating total size of files in a directory
total_size = sum(f.stat().st_size for f in Path('/usr/bin').iterdir())
print(total_size)  # Output: Total size in bytes (example)

# Copying files and folders using shutil
import shutil

# Copying a file
shutil.copy('source_file.txt', 'destination_file.txt')

# Copying an entire folder
shutil.copytree('source_folder', 'destination_folder')

# Moving and renaming files
shutil.move('source_file.txt', 'destination_folder/new_file.txt')

# Deleting files and folders
# unlink() deletes a single file
Path('file_to_delete.txt').unlink()

# rmdir() deletes an empty directory
Path('empty_directory').rmdir()

# rmtree() deletes a directory and all its contents
shutil.rmtree('directory_to_remove')

# Walking a directory tree
# os.walk() generates file names in a directory tree
import os

for folder_name, subfolders, filenames in os.walk('/path/to/dir'):
    print(f'The current folder is {folder_name}')
    for subfolder in subfolders:
        print(f'SUBFOLDER OF {folder_name}: {subfolder}')
    for filename in filenames:
        print(f'FILE INSIDE {folder_name}: {filename}')
    print('')
