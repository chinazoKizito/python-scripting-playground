import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page1 = reader.getPage(0)
    page1.rotateCounterClockwise(270)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page1)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)