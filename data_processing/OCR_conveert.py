import os
import pdfplumber
import fitz  
from PIL import Image
import io
import pytesseract
import cv2
import numpy as np

# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = '//tesseract.'  
def run_ocr(image_path, ocr_engine_path=None):
    """Runs OCR on an image file."""
    if ocr_engine_path is not None:
        pytesseract.pytesseract.tesseract_cmd = ocr_engine_path
    return pytesseract.image_to_string(Image.open(image_path), lang='tir')

def detect_text_in_image(image_path, ratio_threshold=0.02):
    """Detects whether an image likely contains text based on edge density."""
    gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise FileNotFoundError(f"Image file {image_path} not found.")
    
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    edges = cv2.Canny(threshold, 50, 150, apertureSize=3)
    edge_count = np.sum(edges > 0)
    edge_ratio = edge_count / edges.size

    return edge_ratio > ratio_threshold

def extract_images_from_page(pdf_path, page_num, output_dir):
    """Extracts images from a specific PDF page using PyMuPDF (fitz) and saves them."""
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_num)
    image_paths = []

    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
        image_path = os.path.join(output_dir, image_filename)

        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)
        image_paths.append(image_path)

    return image_paths

def process_page(pdf_path, page, page_num, output_dir, ocr_engine_path=None, if_ocr=False):
    """Processes a single PDF page, extracting text and optionally running OCR on images."""
    page_text = page.extract_text()  # Use pdfplumber for text extraction

    if if_ocr:
        image_paths = extract_images_from_page(pdf_path, page_num, output_dir)
        ocr_results = []

        for image_path in image_paths:
            if detect_text_in_image(image_path):
                ocr_text = run_ocr(image_path, ocr_engine_path)
                ocr_results.append(ocr_text)
            else:
                ocr_results.append("")

        if ocr_results:
            page_text = page_text or ""
            page_text += "\n\nOCR Results in This Page:\n" + "\n".join(ocr_results)

    return page_text or ""

def pdf_to_text_with_ocr(pdf_path, output_dir):
    """Converts a PDF to text with optional OCR on images."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = process_page(pdf_path, page, page_num, output_dir, ocr_engine_path='/Users/rahwademoz/tesseract', if_ocr=True)
            text += f"## Page {page_num + 1}\n\n{page_text}\n\n---\n\n"

    return text


pdf_path = 'እቲ ኣልኬምያዊ.pdf'
output_dir = 'output_images'  # Directory to save extracted images
pdf_text = pdf_to_text_with_ocr(pdf_path, output_dir)

# Save to a text file
with open('እቲ ኣልኬምያዊ.txt', 'w', encoding='utf-8') as file:
    file.write(pdf_text)
