import sys
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory

def mergePDF(path, dir):
    # open the files
    pdfFiles = []
    for i in range(len(path)):
        pdfFiles.append(open(path[i], 'rb'))

    # create PDF-Readers for each file
    pdfReaders = []
    for file in pdfFiles:
        pdfReaders.append(PdfFileReader(file))

    # write all pages to writer
    pdfWriter = PdfFileWriter()
    for readers in pdfReaders:
        for pageNum in range(readers.numPages):
            pageObj = readers.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    # write the context into the file
    pdfOutput = open(dir + os.path.sep + 'merged.pdf', 'wb')
    pdfWriter.write(pdfOutput)

    # close the files
    pdfOutput.close()
    for file in pdfFiles:
        file.close()


if __name__ == '__main__':
    # choose the pdf-files and the output directory
    Tk().withdraw()
    filepath = askopenfilenames(filetypes=[('PDF Files', '*.pdf')])
    directory = askdirectory()

    # check if list of filenames and directory path is null
    if not filepath or not directory:
        # exit the program
        sys.exit(0)
    else:
        mergePDF(filepath, directory)
