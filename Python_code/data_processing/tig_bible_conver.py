import pdfplumber

def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Example usage
pdf_path = 'ካብ ምልኪ ናብ ደሞክራሲ.pdf'
pdf_text = pdf_to_text(pdf_path)

# Save to a text file with UTF-8 encoding
with open('ካብ ምልኪ ናብ ደሞክራሲ.txt', 'w', encoding='utf-8') as file:
    file.write(pdf_text)
