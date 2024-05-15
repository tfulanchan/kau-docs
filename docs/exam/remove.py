# Write a Python script to remove all the "© 2016 John Wiley & Sons, Inc." characters in all the markdown files in the same directory of the script

import os

def remove_copyright(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()
        A = "Managing and Using Information Systems: A Strategic Approach – Sixth Edition"
        new_content = content.replace(A, "")
    
    with open(md_file, "w", encoding="utf-8") as file:
        file.write(new_content)
    
    return A

# Get all Markdown files in the current directory
md_files = [file for file in os.listdir() if file.endswith(".md")]

# Remove copyright from each Markdown file
for md_file in md_files:
    removed_text = remove_copyright(md_file)
    print(removed_text + " removal complete.")