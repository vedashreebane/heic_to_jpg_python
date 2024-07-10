import os
import pillow_heif
from PIL import Image

dr = "files"

# Get path of the desired folder
#dr = "files"
# if folder with .heic files the same folder as this .py file
dr = "F:\\files"

# Function to convert the file to desired format
def convert(f):
    heic_file = pillow_heif.read_heif(f)
    image = Image.frombytes(
        heic_file.mode,
        heic_file.size,
        heic_file.data,
        "raw",
    )

    image.save(os.path.join(dr, os.path.basename(f).split('.')[0]) + '.jpg', format="jpeg")
    # for .png conversion - image.save(os.path.join(dr, os.path.basename(f).split('.')[0]) + '.png', format="png")


for f in os.listdir(dr):
    f = os.path.join(dr, f)
    if f.endswith('.heic'):
        convert(f)
