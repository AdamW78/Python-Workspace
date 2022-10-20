from PIL import Image
from pytesseract import pytesseract

tesseract_ocr_path = '/usr/local/Cellar/tesseract/5.2.0/bin/tesseract'


def read_image(image_path) -> str:

    # Opening the image & storing it in an image object
    img = Image.open(image_path)

    # Providing the tesseract
    # executable location to pytesseract library
    pytesseract.tesseract_cmd = tesseract_ocr_path

    # Passing the image object to
    # image_to_string() function
    # This function will
    # extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    return str(text[:-1])