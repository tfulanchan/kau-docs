import os

def convert_to_markdown(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    md_file = os.path.splitext(txt_file)[0] + '.md'
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Converted {txt_file} to {md_file}")

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            txt_file = os.path.join(directory, filename)
            convert_to_markdown(txt_file)

if __name__ == '__main__':
    main()