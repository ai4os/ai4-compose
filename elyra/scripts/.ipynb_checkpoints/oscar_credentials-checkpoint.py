import os
import json


def main():
    credentials = {
        "ID": os.environ.get("ID"),
        "ENDPOINT": os.environ.get("ENDPOINT"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD")
    }

    output_path = "../input/credentials"
    os.makedirs(output_path, exist_ok=True)
    json_path = os.path.join(output_path, os.environ.get("JSON_NAME") + ".json")

    # Si existe el archivo credentials.json, lo borramos
    if os.path.exists(json_path):
        os.remove(json_path)

    # Creamos y escribimos el nuevo archivo credentials.json
    with open(json_path, "w") as f:
        json.dump(credentials, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()