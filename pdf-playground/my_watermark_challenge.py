import PyPDF2
import os
import pdf

merger = PyPDF2.PdfFileMerger()

with open('./super.pdf', mode='rb') as my_file:
    reader = PyPDF2.PdfFileReader(my_file)
    for i in range(reader.numPages):
        page = reader.getPage(i)
        writer = PyPDF2.PdfFileWriter()
        with open('./wtr.pdf', mode='rb') as watermark:
            watermark_file = PyPDF2.PdfFileReader(watermark)
            watermark_page = watermark_file.getPage(0)
            page.mergePage(watermark_page)
            output = PyPDF2.PdfFileWriter()
            output.addPage(page)
            with open(f'watermark/watermarked{i}.pdf', mode='wb') as outfile:
                output.write(outfile)

pdf_list = os.listdir('watermark')
filepath = 'watermark/'
main_list = [filepath + file for file in pdf_list]
pdf.pdf_combiner(main_list, new_file_name='watermarked.pdf')