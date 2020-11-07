import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Users\DELL\AppData\Local\Tesseract-OCR\tesseract.exe'
from gtts import gTTS

# import Os module to start the audio file
import os

img = Image.open('textHand.png')
mytext = tess.image_to_string(img)

report = open('myfile200.txt', 'w')
report.write(mytext)
report.close()
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("output100.mp3")

# Play the converted file
os.system("start output100.mp3")