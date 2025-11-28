#https://www.facebook.com/100064326836270/posts/1300128825474666/?rdid=FdJaRXwHIQ1bZDSa#
#https://www.clcoding.com/search?q=Remove+Image+Background+in+Python

# Files to be saved in - C:\Prasanna\Personal\Education-Technical\Python-Beginner10Functions\
#pip install rembg pillow
#pip install onnxruntime

from rembg import remove
from PIL import Image   

#cannot write mode RGBA as JPEG
input_path  = "1_picture_with_background.jpg"
output_path = "1_picture_without_background.png"
inputfile = Image.open(input_path)
outputfile = remove(inputfile)  
outputfile.save(output_path)
