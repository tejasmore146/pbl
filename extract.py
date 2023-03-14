from PyPDF2 import PdfReader


file = "CAPR-III_6207.pdf"

reader = PdfReader(file)
page = reader.pages[0]

# Open a file in write mode
with open('file.txt', 'w') as f:
    f.write(page.extract_text())
    


