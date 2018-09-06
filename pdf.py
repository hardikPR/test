import PyPDF2
pdf_file = open('/home/hardik/Desktop/sample.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader('/home/hardik/Desktop/sample.pdf')
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print page_content