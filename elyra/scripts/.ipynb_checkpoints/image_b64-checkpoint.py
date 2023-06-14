import os
import base64
from pathlib import Path


def main():
    image_name = os.environ.get("IMAGE_INPUT")
    if not image_name:
        print("La variable de entorno IMAGE no está establecida. Abortando.")
        return

    input_path = Path("../input/images")
    output_path = Path("../input/data")
    output_path.mkdir(parents=True, exist_ok=True)

    input_file = input_path / image_name
    output_file = output_path / f"{image_name.rsplit('.', 1)[0]}.txt"

    if not input_file.is_file():
        print(f"El archivo {input_file} no existe. Abortando.")
        return

    # Si existe el archivo de salida, lo borramos
    if output_file.is_file():
        output_file.unlink()

    with open(input_file, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())

    with open(output_file, "wb") as txt_file:
        txt_file.write(encoded_image)

    print(f"Imagen {image_name} convertida a base64 y guardada en {output_file}")


if __name__ == "__main__":
    main()
