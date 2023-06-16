import os
import base64
from pathlib import Path


def main():
    # Get the image name from the environment variable
    image_name = os.environ.get("IMAGE_INPUT")
    if not image_name:
        print("The IMAGE_INPUT environment variable is not set. Aborting.")
        return

    # Define input and output paths relative to the current directory
    input_path = Path("./images")
    output_path = Path("./data")

    # Create the output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    input_file = input_path / image_name
    output_file = output_path / f"{image_name.rsplit('.', 1)[0]}.txt"

    # Check if the input file exists
    if not input_file.is_file():
        print(f"El archivo {input_file} no existe. Abortando.")
        return

    # If the output file exists, delete it
    if output_file.is_file():
        output_file.unlink()

    # Open the image file, encode it in base64, and write the result to the output file
    with open(input_file, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())

    with open(output_file, "wb") as txt_file:
        txt_file.write(encoded_image)

    print(f"Image {image_name} converted to base64 and saved at {output_file}")


if __name__ == "__main__":
    main()
