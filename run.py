import pytesseract             #Importing ocr framework
from PIL import Image          #Importing image framework to load image
import pyttsx3
engine = pyttsx3.init() # object creation


#This is the function for making the computer to talk
def talk_function(text):
    engine.say(text)
    engine.runAndWait()



voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female | 0 for male


# This is the main function which convets the image into digital text format.
def ocr_core(image_name):
    text = pytesseract.image_to_string(Image.open(image_name))  
    return text


#Testing the project
returnText =  ocr_core("test_image_2.png")

talk_function(returnText)           #testing Done

