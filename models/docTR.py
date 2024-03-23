import os
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

os.environ['USE_TORCH'] = '1'
model = ocr_predictor(pretrained=True)
# PDF

start_path = '../images/'

# get all images from ../images/ folder
images = os.listdir(start_path)

for image in images:
    # open image
    img = DocumentFile.from_images(start_path + image)
    # extract text
    result = model(img)
    # print text
    print(f'{image}: {result.show()}')
