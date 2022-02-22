from PyPDF2 import PdfFileWriter, PdfFileReader
import pdfplumber


input_file = "input/input.pdf"
input_pdf = PdfFileReader(input_file)

def invoice_number(page_number):
    with pdfplumber.open(input_file) as pdf:
        page = pdf.pages[page_number]
        text = page.extract_text()
    lines = text.split('\n')
    line = lines[4]
    words = line.split(' ')
    invo_num = words[-2]
    return invo_num

for i in range(input_pdf.numPages):
    page_number = i + 1
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(i))
    invo_number = invoice_number(i)
    with open("output/invoice-%s.pdf" % invo_number, "wb") as outputStream:
        output.write(outputStream)
        print(f"{page_number}. PDF invoice-{invo_number} is Created.")



