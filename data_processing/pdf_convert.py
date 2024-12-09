import pdfplumber
import re

def pdf_to_text(file_path, output_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    with open(output_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

pdf_to_text("ካብ ምልኪ ናብ ደሞክራሲ.pdf", "ካብ ምልኪ ናብ ደሞክራሲ.txt")