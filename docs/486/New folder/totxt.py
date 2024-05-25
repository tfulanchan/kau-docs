import os

# Get the current directory
dir_path = os.getcwd()

# Loop through all the files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a .md file
    if filename.endswith('.md'):
        # Get the new file name with the .txt extension
        new_filename = os.path.splitext(filename)[0] + '.txt'
        # Rename the file
        os.rename(filename, new_filename)