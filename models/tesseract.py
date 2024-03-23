import pytesseract
from PIL import Image
import os

# get all images from ../images/ folder
images = os.listdir('../images/')

# loop through all images
for image in images:
    # open image
    img = Image.open(f'../images/{image}')
    # extract text
    text = pytesseract.image_to_string(img)
    # print text
    print(f'{image}: {text}')