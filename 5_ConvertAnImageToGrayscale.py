#https://www.facebook.com/watch/?v=1160587889476948

# Files to be saved in - C:\Prasanna\Personal\Education-Technical\Python-Beginner10Functions\
#pip install pillow

from PIL import Image   

original_image  = "5_ConvertAnImageToGrayscale.jpg"
img = Image.open(original_image)
gray = img.convert('L')
gray.save("5_ConvertAnImageToGrayscale_Gray.jpg")
gray.show()
