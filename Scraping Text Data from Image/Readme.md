# Scraping Text Data from Invoice
![Python 3.9](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![NLTK](https://img.shields.io/badge/Library-NLTK-orange.svg) ![PIL](https://img.shields.io/badge/PIL-1.1.7-blueviolet) ![pytesseract](https://img.shields.io/badge/pytesseract-0.3.4-yellow)


## **Introduction**
This project demonstrates how to extract and process text from invoice images using **Python**, **pytesseract**, and **Pillow**. It automates the process of reading invoices and converting the information into a structured dictionary format for easy data handling. The extracted data can be further used for financial record-keeping, auditing, or integrating into databases.


## **Features**
- Extracts text data from images using **Tesseract OCR**.
- Splits and cleans the extracted text for structured processing.
- Stores extracted details in a **dictionary** with key-value pairs for:
  - Items
  - Dates
  - Amounts
  - Reasons
- Customizable preprocessing for different invoice formats.


### View ScreenRecording for Live Demo:
<img src="https://github.com/amark720/Computer-Vision-and-OpenCV-Projects/blob/main/Scraping%20Text%20Data%20from%20Image/InvoiceToText%20Recording.gif" width=90% height=90% >


## **Installation Instructions**
#### Step 1: Clone the Repository
```bash
git clone https://github.com/amark720/Computer-Vision-and-OpenCV-Projects.git
cd "Scraping Text Data from Image"
```

#### Step 2: Install Required Libraries
Install the necessary Python libraries:
```bash
pip install pytesseract pillow
```

#### Step 3: Install Tesseract OCR
Download and install **Tesseract OCR** from [HERE](https://github.com/tesseract-ocr/tesseract):
- Use the installer: `tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64-bit)`
- During installation, note the installation directory for later use.

#### Step 4: Update Paths in Code
- Update the `tesseract_cmd` variable in the code with the path to your `tesseract.exe` file.
- Provide the path to the invoice image you wish to process.


## **Technologies Used**
- **Programming Language:** Python 3.9
- **OCR Tool:** Tesseract OCR
- **Libraries:**
  - `pytesseract`: For extracting text from images.
  - `Pillow`: For image loading and manipulation.


## **How to Use**
1. **Prepare the Invoice Image:**
   - Place your invoice image in a known directory.
   - Ensure the text in the image is clear and legible.

2. **Run the Script:**
   ```bash
   python OCR_Invoice_to_Text.py
   ```

3. **Customize Text Preprocessing:**
   - Modify the text cleaning logic to suit your invoice format.
   - Update indices in the code if the invoice structure changes.

4. **Output:**
   - Extracted data is displayed in the console as a structured dictionary:
     ```json
     {
         "Items": [...],
         "Date": [...],
         "Amount": [...],
         "Reason": [...]
     }
     ```


## **Areas of Further Improvement**
- **Invoice Format Detection:**
  - Add automatic detection and customization for different invoice templates.
- **GUI Integration:**
  - Build a user-friendly interface for uploading images and displaying results.
- **Database Storage:**
  - Save the extracted data directly to a database for long-term use.
- **Batch Processing:**
  - Enable processing of multiple invoices simultaneously.


## **Conclusion**
This project provides a foundation for extracting and organizing data from invoice images using OCR. It is customizable and can be scaled for various business needs, such as automating financial data entry.


## **Acknowledgments**
- Thanks to the **Tesseract OCR** team for providing a powerful open-source OCR tool.
- Special thanks to the developers of **Pillow** and **pytesseract** libraries for seamless Python integrations.


#### 📧 Feel Free to contact me at➛ **amark720@gmail.com** for any assistance or questions related to this project!
