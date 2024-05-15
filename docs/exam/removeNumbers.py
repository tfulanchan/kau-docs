import os
import re

def remove_numbers(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    new_content = re.sub(r'\d+', '', content)
    
    with open(md_file, "w", encoding="utf-8") as file:
        file.write(new_content)

# Get all Markdown files in the current directory
md_files = [file for file in os.listdir() if file.endswith(".md")]

# Remove numbers from each Markdown file
for md_file in md_files:
    remove_numbers(md_file)

print("Number removal complete.")