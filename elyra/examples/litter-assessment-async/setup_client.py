#libraries
import os
import pickle
import subprocess
import sys
import pathlib
import json
from urllib.parse import urlparse

# Install required dependencies locally
required_packages = ["oscar-python", "liboidcagent"]
for package in required_packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

# Update PYTHONPATH to include user site-packages
user_site = subprocess.check_output([sys.executable, "-m", "site", "--user-site"], text=True).strip()
sys.path.append(user_site)

# Import oscar_python after ensuring it's in PYTHONPATH
try:
    from oscar_python.client import Client
except ModuleNotFoundError:
    raise RuntimeError("Failed to import oscar_python after installation. Ensure the package is installed correctly.")
# Environment variables
endpoint = os.getenv("OSCAR_ENDPOINT", "https://default-endpoint.com")
cluster_id = os.getenv("OSCAR_CLUSTER_ID", "OSCAR")
config_archive= os.getenv("CONFIG_ARCHIVE", "minio_config.pkl")
type_invocation= os.getenv("TYPE_INVOCATION", "sync")
if not config_archive.endswith(".pkl"):
    config_archive += ".pkl"
token_file_path = os.getenv("TOKEN", "")
token = token_file_path
# Configure OSCAR client
options_oidc_auth = {
    'cluster_id': cluster_id,
    'endpoint': endpoint,
    'oidc_token': token,
    'ssl': True
}
try:
    client = Client(options=options_oidc_auth)
    print("OSCAR client configured successfully.")
    if type_invocation=='sync':
        with open(config_archive, "wb") as client_file:
            pickle.dump(client, client_file)
        print(f"Saved configuration {type_invocation} in {config_archive}")
    elif type_invocation=='async':
        try:
            info = client.get_cluster_config()
            data = json.loads(info.text)
            parsed_url = urlparse(data['minio_provider']['endpoint'])
            host = parsed_url.netloc
            config = {
                "endpoint": host,
                "access_key": data['minio_provider']['access_key'],
                "secret_key": data['minio_provider']['secret_key'],
                #"secure": secure
             }
            with open(config_archive, "wb") as f:
                pickle.dump(config, f)
            print(f"Saved configuration {type_invocation} in {config_archive}")
        except Exception as err:
            print("Failed with: ", err)
    else:
        print(f"Error with TYPE_INVOCATION")
except Exception as e:
    raise RuntimeError(f"Error configuring OSCAR client: {e}")

