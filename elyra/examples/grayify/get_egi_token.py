import base64
import os

def encode_token(token):
    """
    Encodes the given token using Base64.

    Parameters:
    token (str): The token to encode.

    Returns:
    bytes: The Base64 encoded token.
    """
    return base64.b64encode(token.encode())

def save_encoded_token(encoded_token, output_path):
    """
    Saves the encoded token to the specified path.

    Parameters:
    encoded_token (bytes): The encoded token to save.
    output_path (str): The file path where the encoded token should be saved.
    """
    with open(output_path, 'wb') as file:
        file.write(encoded_token)

if __name__ == "__main__":
    # Path to the access token file
    token_file_path = "/var/run/secrets/egi.eu/access_token"
    # Output directory for the encoded token file
    output_dir = os.getenv("ENCODED_TOKEN_DIR", "./")
    # Output file name for the encoded token
    output_file_name = os.getenv("ENCODED_TOKEN_FILE", "encoded_access_token.txt")
    # Full output path
    output_path = os.path.join(output_dir, output_file_name)

    # Read the access token
    with open(token_file_path) as f:
        access_token = f.read()

    # Encode the token
    encoded_token = encode_token(access_token)

    # Save the encoded token
    save_encoded_token(encoded_token, output_path)

    print(f"Encoded token saved to {output_path}")
