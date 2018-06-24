from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
image = Image.open('C:\\temp\\pl_no69435.jpg')
text= pytesseract.image_to_string(image)
print(text)


