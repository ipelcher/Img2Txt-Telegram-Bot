import cv2
import pytesseract

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Configurating Tesseract
config = r'--oem 3 --psm 6'

def textFromImg(img):

    # Adding an image
    img = cv2.imread(img)
    # Converting photo colors from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reading text from the photo
    datatext = pytesseract.image_to_string(img, config=config)[:-1]


    return datatext
