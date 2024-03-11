import os
import base64

def convert_image_to_base64(input_image_name, output_file_name, input_dir, output_dir):
    """
    Converts an image to base64 format and saves it to a specified location.
    
    Parameters:
    input_image_name (str): The name of the input image.
    output_file_name (str): The name for the output file to save the base64-encoded image.
    input_dir (str): Directory where the input image is located.
    output_dir (str): Directory where the base64-encoded image will be saved.
    """
    input_image_path = os.path.join(input_dir, input_image_name)
    output_file_path = os.path.join(output_dir, output_file_name)
    
    try:
        # Read the image and encode it to base64
        with open(input_image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        # Save the base64-encoded image to the specified output file
        with open(output_file_path, 'w') as file:
            file.write(encoded_string)
        
        print("The image has been successfully converted to base64 and saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Retrieve the environment variables
    input_image_name = os.environ.get("IMAGE_INPUT", "default_input_image.jpg")
    output_file_name = os.environ.get("BASE64_OUTPUT", "default_output.txt")
    input_dir = os.environ.get("INPUT_DIR", "./")  # Default to current directory
    output_dir = os.environ.get("OUTPUT_DIR", "./")  # Default to current directory
    
    # Convert the image and save it
    convert_image_to_base64(input_image_name, output_file_name, input_dir, output_dir)
