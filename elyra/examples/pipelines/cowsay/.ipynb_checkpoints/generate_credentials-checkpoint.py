import os
import json


def main():
    # Retrieve environment variables and store them in a dictionary
    credentials = {
        "ID": os.environ.get("ID"),
        "ENDPOINT": os.environ.get("ENDPOINT"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD")
    }

    # Set the output path to a "credentials" directory in the current directory
    output_path = "./credentials"
    
    # Create the "credentials" directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Create the JSON file path, using the "JSON_NAME" environment variable
    json_path = os.path.join(output_path, os.environ.get("JSON_NAME") + ".json")

    # If the credentials JSON file already exists, delete it
    if os.path.exists(json_path):
        os.remove(json_path)

    # Create and write to the new credentials JSON file
    with open(json_path, "w") as f:
        json.dump(credentials, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()