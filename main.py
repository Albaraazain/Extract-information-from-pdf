import fitz  # PyMuPDF

def extract_text_with_positions(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    if doc is None:
        print("Error in opening")

    # Loop through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Get text blocks
        text_blocks = page.get_text("dict")["blocks"]

        for block in text_blocks:
            if block["type"] == 0:  # Block contains text
                bbox = block["bbox"]  # Bounding box
                text = block["lines"]

                # Print text and its bounding box
                print(f"Text Block Bounding Box: {bbox}")
                for line in text:
                    print(" ".join([span["text"] for span in line["spans"]]))
                print()

    doc.close()

# Usage
extract_text_with_positions("./pdf/trialPDF3.pdf")
