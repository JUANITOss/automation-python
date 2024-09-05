import os

# Expand the '~' to the full home directory path
path = os.path.expanduser(r"~/Workspace/automation-python")

for folderName, subFolders, filenamesInFolder in os.walk(path):
    
    if folderName != (path + ""):
        print("this is the folder: " + folderName)
        print("these are sub-folders: " + str(subFolders))
        print("these are the files in the current folder: " + str(filenamesInFolder))        
    
    # Remove subfolders containing 'fish'
    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(os.path.join(folderName, subfolder))

    # Copy '.py' files with a '.backup' extension
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))
