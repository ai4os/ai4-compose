import os
import pytesseract
from PIL import Image

# Obtain name from image file in the enviroment variable
image_input = os.getenv('IMAGE_INPUT')

# Complete path of the image
image_path = f"./images/{image_input}.jpg"

# Read image
image = Image.open(image_path)

# Extract text from the image using Tesseract OCR
extracted_text = pytesseract.image_to_string(image)

# Obtain name from data output file in the enviroment variable
data_output = os.getenv('DATA_OUTPUT')

# Create output directory if doesn't exist
os.makedirs('../output/data', exist_ok=True)

# Complete path from data output file
data_output_path = f"../output/data/{data_output}.txt"

# Save the text extracted from the text file
with open(data_output_path, 'w') as f:
    f.write(extracted_text)
