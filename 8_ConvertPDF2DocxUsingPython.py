#Convert PDF to docx using Python
#https://www.facebook.com/pythonclcoding/posts/pfbid0MvEUZz6g4kT8adriupH1M8x2rGiDZneBuVfAaFnDPnRJxdDGMNqF2oVM3SqBzYzxl

#pip install pdf2docx
from pdf2docx import Converter
pdf_file  = '8_ConvertPDF2DocxUsingPython.pdf'
docx_file = '8_ConvertPDF2DocxUsingPython.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default   
cv.close() 
