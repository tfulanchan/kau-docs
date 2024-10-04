import os
import glob
from datetime import datetime

# Get all .png files in the current directory
png_files = glob.glob("*.png")

# Sort files by creation time
png_files.sort(key=os.path.getctime)

# Rename files with the pattern ch03-1, ch03-2, ...
for index, file_name in enumerate(png_files, start=1):
    # Construct new file name
    new_name = f"ch03-{index}.png"
    
    # Rename the file
    os.rename(file_name, new_name)

    # Output the renaming process
    print(f"Renamed: {file_name} -> {new_name}")

print("Renaming complete!")
