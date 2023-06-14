import os
import pytesseract
from PIL import Image

# Obtener el nombre del archivo de imagen de la variable de entorno
image_input = os.getenv('IMAGE_INPUT')

# Ruta completa de la imagen
image_path = f"../output/images/{image_input}.jpg"

# Leer la imagen
image = Image.open(image_path)

# Extraer el texto de la imagen utilizando Tesseract OCR
extracted_text = pytesseract.image_to_string(image)

# Obtener el nombre del archivo de salida de datos de la variable de entorno
data_output = os.getenv('DATA_OUTPUT')

# Crear el directorio de salida si no existe
os.makedirs('../output/data', exist_ok=True)

# Ruta completa del archivo de salida de datos
data_output_path = f"../output/data/{data_output}.txt"

# Guardar el texto extraído en un archivo de texto
with open(data_output_path, 'w') as f:
    f.write(extracted_text)
