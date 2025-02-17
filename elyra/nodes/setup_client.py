import os
import pickle
import subprocess
import sys

required_packages = ["oscar-python", "liboidcagent"]
for package in required_packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])

# Update PYTHONPATH to include user site-packages
user_site = subprocess.check_output([sys.executable, "-m", "site", "--user-site"], text=True).strip()
sys.path.append(user_site)

try:
    from oscar_python.client import Client
except ModuleNotFoundError:
    raise RuntimeError("Failed to import oscar_python after installation. Ensure the package is installed correctly.")

endpoint = os.getenv("OSCAR_ENDPOINT", "https://inference.cloud.ai4eosc.eu")
cluster_id = os.getenv("OSCAR_CLUSTER_ID", "OSCAR")
token_file_path = os.getenv("TOKEN_FILE_PATH", "/var/run/secrets/egi.eu/access_token")

try:
    with open(token_file_path, 'r') as token_file:
        token = token_file.read().strip()
except FileNotFoundError:
    raise FileNotFoundError(f"Token file not found at {token_file_path}.")

options_oidc_auth = {
    'cluster_id': cluster_id,
    'endpoint': endpoint,
    'oidc_token': token,
    'ssl': True
}

try:
    client = Client(options=options_oidc_auth)
    print("OSCAR client configured successfully.")
except Exception as e:
    raise RuntimeError(f"Error configuring OSCAR client: {e}")

with open("client.pkl", "wb") as client_file:
    pickle.dump(client, client_file)
    print("Client saved as client.pkl.")
