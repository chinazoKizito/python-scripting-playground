from PyPDF2 import PdfFileMerger
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list, new_file_name):
    merger = PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(new_file_name)


pdf_combiner(inputs, new_file_name='super.pdf')
