import pypdf 
import pandas as pd

pdftext = []

with open('INV-1000.pdf', 'rb') as file:
    reader = pypdf.PdfReader(file)
    num_pages = len(reader.pages)
    print(f"Number of pages: {num_pages}")
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(len(text))
        print(f"\n--- Page {page_num + 1} ---")
        print(text)
        pdftext.append(text)


print(pdftext)