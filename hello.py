from PIL import Image
from pytesseract import pytesseract
import enum

class ImageReader:
    def __init__(self):
        windows_path=r'C:\Users\Suraj S\PycharmProjects\med\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd=windows_path

    def extract_text(self,image:str,lang:str)-> str:
        img=Image.open(image)
        extracted = pytesseract.image_to_string(img,lang=lang)
        return extracted

if __name__ == '__main__':
    ir=ImageReader()
    text = ir.extract_text('med2.jpg',lang='eng')
    print(text)