import os
import re
import fitz
import requests

img_path = ".\download\\"
doc = fitz.open()


def img2pdf(name, num):
	for i in range(1,num):
		num = str(i).rjust(3, '0')
		img = f"{str(name)}_{str(num)}.jpg"
		img_file = img_path + img
		imgdoc = fitz.open(img_file)
		pdfbytes = imgdoc.convertToPDF()
		pdf_name = str(i) + '.pdf'
		imgpdf = fitz.open(pdf_name, pdfbytes)
		doc.insertPDF(imgpdf)
	doc.save('combined.pdf')
	doc.close()

if __name__ == "__main__":
	img2pdf("9781292244877", 224)