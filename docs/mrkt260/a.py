import re
import os

def correct_question_numbers():
    # Automatically find the .txt file in the current directory (case-insensitive)
    file_path = None
    for filename in os.listdir('.'):
        if filename.lower().endswith('.txt'):
            file_path = filename
            break

    if not file_path:
        print("No .txt file found in the current directory.")
        return

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.readlines()

    corrected_lines = []
    question_count = 1

    # Regular expression to match question lines
    question_pattern = re.compile(r'^\d+\.\s+')

    for line in content:
        # Check if line matches a question pattern
        if question_pattern.match(line):
            # Replace current number with the correct question number
            corrected_line = re.sub(r'^\d+\.', f'{question_count}.', line)
            corrected_lines.append(corrected_line)
            question_count += 1
        else:
            corrected_lines.append(line)

    # Write corrected content back to a new file
    corrected_file_path = f'corrected_{file_path}'
    with open(corrected_file_path, 'w') as file:
        file.writelines(corrected_lines)

    print(f"Questions renumbered successfully. Check '{corrected_file_path}' for the output.")

# Run the function
correct_question_numbers()
