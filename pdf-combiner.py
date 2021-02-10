#Requires command: "pip install PyPDF2"

import PyPDF2
import sys

inputs = sys.argv[1:]

def combiner(pdf_list):
    try:
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write('super.pdf')
    except:
        print('Please only input paths to pdf files.')


combiner(inputs)
