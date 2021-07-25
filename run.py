import pytesseract             #Importing ocr framework
from PIL import Image          #Importing image framework to load image


def ocr_core(image_name):
    text = pytesseract.image_to_string(Image.open(image_name))  
    return text
