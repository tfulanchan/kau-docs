import os
import PyPDF2

def pdf_to_md(pdf_file):
    with open(pdf_file, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
            if page_num < len(pdf_reader.pages) - 1:
                text += "\n" + "=" * 80 + "\n"
    
    md_file = os.path.splitext(pdf_file)[0] + ".md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(text)

# Get all PDF files in the current directory
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

# Convert each PDF file to MD
for pdf_file in pdf_files:
    pdf_to_md(pdf_file)

print("PDF to MD conversion complete.")