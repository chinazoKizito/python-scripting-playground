import PyPDF2

# Aneagoie's cleaner solution
template = PyPDF2.PdfFileReader(open('./super.pdf'))
watermark = PyPDF2.PdfFileReader(open('./wtr.pdf.pdf'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
with open('watermarked_output.pdf', 'wb') as external:
    output.write(external)
