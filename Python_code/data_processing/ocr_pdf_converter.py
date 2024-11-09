class PDFConverter:
    def __init__(self, pdf_path, output_dir, ocr_engine_path=None):
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        self.ocr_engine_path = ocr_engine_path

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


    def extract_images_from_page(self, page, page_num):
        """
        Extracts images from a single PDF page and saves them.

        Args:
        page: The PyMuPDF page object.
        page_num (int): Page number for naming images.

        Returns:
        list: List of image file paths.
        """
        images = page.get_images(full=True)
        image_paths = []

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = page.parent.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page_{page_num + 1}_img_{img_index + 1}.{image_ext}"
            image_path = os.path.join(self.output_dir, image_filename)

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            image_paths.append(image_path)

        return image_paths

    def process_page(self, page, page_num, if_ocr=False):
        """
        Processes a single page, extracting text and images, and appending OCR results.

        Args:
        page: The PyMuPDF page object.
        page_num (int): Page number.

        Returns:
        str: Markdown content for the page.
        """
        # Step 1: Extract text from the page
        page_text = page.get_text("text")

        # Step 2 (Optional): Extract images and run OCR
        if if_ocr:
            
            image_paths = self.extract_images_from_page(page, page_num)
            ocr_results = []

            for image_path in image_paths:
                if detect_text_in_image(image_path):
                    ocr_text = run_ocr(image_path, self.ocr_engine_path)
                    ocr_results.append(ocr_text)
                else:
                    ocr_results.append("")

            # Step 3 (Optional): Append OCR results to the page text
            if ocr_results:
                page_text += "\n\nOCR Results in This Page:\n"
                page_text += "\n".join(ocr_results)

        return page_text

    def convert_pdf_to_markdown_with_ocr(self):
        """
        Converts the PDF to markdown, with text and OCR results at the bottom of each page.

        Returns:
        str: Path to the generated markdown file.
        """
        doc = fitz.open(self.pdf_path)
        markdown_content = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_markdown = self.process_page(page, page_num, if_ocr=True)
            markdown_content.append(f"## Page {page_num + 1}\n\n" + page_markdown)

        # Combine all pages and save the markdown file
        final_markdown = "\n\n---\n\n".join(markdown_content)
        markdown_path = os.path.join(self.output_dir, os.path.splitext(os.path.basename(self.pdf_path))[0] + '.md')

        with open(markdown_path, 'w', encoding='utf-8') as md_file:
            md_file.write(final_markdown)

        return markdown_path
    
    def convert_pdf_to_markdown_without_ocr(self):
        """
        Converts the PDF to markdown, with text and OCR results at the bottom of each page.

        Returns:
        str: Path to the generated markdown file.
        """
        doc = fitz.open(self.pdf_path)
        markdown_content = []

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            page_markdown = self.process_page(page, page_num, if_ocr=False)
            markdown_content.append(f"## Page {page_num + 1}\n\n" + page_markdown)

        # Combine all pages and save the markdown file
        final_markdown = "\n\n---\n\n".join(markdown_content)
        markdown_path = os.path.join(self.output_dir, os.path.splitext(os.path.basename(self.pdf_path))[0] + '.md')

        with open(markdown_path, 'w', encoding='utf-8') as md_file:
            md_file.write(final_markdown)

        return markdown_path