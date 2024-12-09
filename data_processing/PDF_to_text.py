# Importing the pdfplumber library for extracting text from PDF files
import pdfplumber

# Function to extract text from a PDF file
def pdf_to_text(pdf_path):
    # Initialize an empty string to store the extracted text
    text = ""
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through all pages in the PDF
        for page in pdf.pages:
            # Extract text from the current page
            page_text = page.extract_text()
            # Append the extracted text to the final string if it's not empty
            if page_text:
                text += page_text + "\n"
    # Return the combined text from all pages
    return text

# Example usage of the function
pdf_path = 'Tigirinya_bible.pdf'  # Path to the input PDF file
pdf_text = pdf_to_text(pdf_path)  # Extract text from the PDF

# Save the extracted text to a text file with UTF-8 encoding
with open('Tigirinya_bible.txt', 'w', encoding='utf-8') as file:
    file.write(pdf_text)
