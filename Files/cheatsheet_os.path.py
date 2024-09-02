# Files have a name and a path. 
# The root folder is the lowest folder.
# On Windows, it's C:\ and on Linux/Mac, it's /.
# In a file path, folders and filenames are separated by backslashes on Windows
# and forward slashes on Linux/Mac.
# Use os.path.join() to combine folders with the correct slash.

import os

# Get the current working directory
current_directory = os.getcwd()

# Change the working directory
os.chdir('/new/path')

# Absolute paths start with the root folder, relative paths do not.
# The '.' folder represents the current folder and '..' represents the parent folder.

# Get an absolute path
absolute_path = os.path.abspath('myfile.txt')

# Check if a path is absolute
is_absolute = os.path.isabs('/some/path')

# Get a relative path between two paths
relative_path = os.path.relpath('/path/to/file', '/another/path')

# Make a new directory
os.makedirs('/new/folder')

# Get a file's size
file_size = os.path.getsize('myfile.txt')

# List files in a directory
files = os.listdir('/some/folder')

# Check if a file or directory exists
exists = os.path.exists('/path/to/check')

# Check if a path is a file
is_file = os.path.isfile('/some/file')

# Check if a path is a directory
is_dir = os.path.isdir('/some/directory')
