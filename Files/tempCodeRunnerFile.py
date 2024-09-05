import os

for folderName, subFolders, filenamesInFolder in os.walk(r"~/Workspace"):
    print("this is the folder: " + folderName)
    print("these are sub-folders: " + str(subFolders))
    print("these are the files in the current folder: " + str(filenamesInFolder))