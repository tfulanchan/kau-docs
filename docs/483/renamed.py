import os

# Get the current directory
directory = os.getcwd()

# List all .png files in the directory
png_files = [f for f in os.listdir(directory) if f.endswith('.png')]

# Initialize a counter for the new filenames
counter = 1

# Rename each file according to the specified pattern
for filename in png_files:
    # Create the new filename
    new_filename = f"ch02-{counter}.png"
    
    # Construct full file paths
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_filename)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    
    print(f"Renamed '{filename}' to '{new_filename}'")
    
    # Increment the counter for the next file
    counter += 1

print("Renaming completed.")