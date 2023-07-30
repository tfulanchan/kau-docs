import os

def list_large_files(directory):
    large_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > 50 * 1024 * 1024:  # 50 MB in bytes
                large_files.append(file_path)
    return large_files

directory = "."  # Change this to the directory you want to check
large_files = list_large_files(directory)
if large_files:
    print("Large files found:")
    for file in large_files:
        print(file)
else:
    print("No large files found.")