import pytesseract             #Importing ocr framework
from PIL import Image          #Importing image framework to load image


# This is the main function which convets the image into digital text format.
def ocr_core(image_name):
    text = pytesseract.image_to_string(Image.open(image_name))  
    return text


#Testing the project
print(ocr_core("test_image_2.png"))
