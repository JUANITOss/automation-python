import os
import shutil

# Ensure the 'txts' directory exists
os.makedirs('./txts', exist_ok=True)

# Makes the copy 
shutil.move( './example.txt', './txts/example1.txt' )