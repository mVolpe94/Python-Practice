#Requires command: "pip install PyPDF2"

import PyPDF2
import sys

pdf_list = sys.argv[2:]
watermark = sys.argv[1]

def watermarker(file, watermark):
    with open(watermark, 'rb') as wtrmrk:
        wtr_pdf = PyPDF2.PdfFileReader(wtrmrk)
        wtr = wtr_pdf.getPage(0)
        writer = PyPDF2.PdfFileWriter()
        with open(f'wtr-{file}', 'wb') as wtrfile:
            with open(file, 'rb') as nowtr:
                pdf = PyPDF2.PdfFileReader(nowtr)
                pages = pdf.getNumPages()
                for page in range(pages):
                    cur_page = pdf.getPage(page)
                    cur_page.mergePage(wtr)
                    writer.addPage(cur_page)
                writer.write(wtrfile)
                nowtr.close()


for file in pdf_list:
    watermarker(file, watermark)



# with open('super.pdf', 'rb') as ofile:
#     old_file = PyPDF2.PdfFileReader(ofile)
#     pages = old_file.numPages
#     print(pages)
