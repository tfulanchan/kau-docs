import os

def replace_chars(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    new_content = content.replace("•", "+ ")
    
    with open(md_file, "w", encoding="utf-8") as file:
        file.write(new_content)

# Get all Markdown files in the current directory
md_files = [file for file in os.listdir() if file.endswith(".md")]

# Replace characters in each Markdown file
for md_file in md_files:
    replace_chars(md_file)

print("Character replacement complete.")