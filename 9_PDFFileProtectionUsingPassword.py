#PDF file protection using password in Python
#https://www.facebook.com/pythonclcoding/posts/pfbid02f5MVnEhp6YW1Qi9EqEnzMt78kfWxsvPjfgTEdmnyDhULA7g7Rs7S7nP3shgYzhwfl

#pip install PyPDF2

from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Copy all pages to writer
    for page in reader.pages:
        writer.add_page(page)

    # Get password from user
    password = getpass.getpass("Enter a password to protect the PDF: ")

    # Encrypt the PDF with the provided password
    writer.encrypt(password)

    # Write the protected PDF to a new file
    with open(output_pdf, 'wb') as f:
        writer.write(f)

    print(f"Protected PDF saved as: {output_pdf}")

#Password: helloworld
protect_pdf('9_PDFFileProtectionUsingPasswordSource.pdf', '9_PDFFileProtectionUsingPasswordProtected.pdf')
