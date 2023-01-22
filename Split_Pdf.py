import os
from PyPDF2 import PdfFileWriter, PdfFileReader

a=os.getcwd()
print('current directory:- ',a)
b=os.listdir(a)
print('Files in the directory:- ',b)
for filename in os.listdir(a):
	if filename.endswith('.pdf'):
		inputpdf = PdfFileReader(open(filename, "rb"))

		for i in range(inputpdf.numPages):
			output = PdfFileWriter()
			output.addPage(inputpdf.getPage(i))
			with open("document-page%s.pdf" % i, "wb") as outputStream:
				output.write(outputStream)
				print('Writing data.... document-page%s.pdf' % i)