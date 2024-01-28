# PDF Text and Position Extractor

This project provides a Python script that extracts text along with its bounding box positions from a PDF file using the PyMuPDF library.

## Features

- **PDF Text Extraction**: Extracts text from each page of the PDF.
- **Bounding Box Information**: Retrieves the bounding box for each text block, providing spatial information of text on the page.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- PyMuPDF library installed. You can install it using `pip`:
  
  ```bash
  pip install PyMuPDF
  ```

## Installation

To use this script, simply clone this repository or download the script to your local machine.

## Usage

To run the script, navigate to the script's directory and use the following command:

```bash
python extract_text_with_positions.py
```

Make sure to replace `"./pdf/trialPDF3.pdf"` in the script with the path to your target PDF file.

## How It Works

The script performs the following operations:

1. Opens the specified PDF file.
2. Iterates through each page of the PDF.
3. For each page, it retrieves text blocks along with their bounding boxes.
4. Prints the text of each block and the corresponding bounding box coordinates to the console.

## Example Output

```
Text Block Bounding Box: [x0, y0, x1, y1]
Extracted Text Line 1
Extracted Text Line 2
...
```

## Contributing

If you'd like to contribute to this project, your ideas and improvements are welcome. Please fork the repository and create a pull request, or simply open an issue with the tag "enhancement".

## License

This project is free to use and does not require a license.
