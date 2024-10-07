import PyPDF2

pdfiles = ["1.pdf" , "2.pdf" , "3.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename , 'rb')
    pdfreader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfreader)
pdfFile.close()
merger.write("merged.pdf")
