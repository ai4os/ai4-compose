import base64
import json
import os
import paho.mqtt.client as mqtt
import requests
from minio import Minio

# --- Initial Configuration ---
OSCAR_SERVER = ""
USERNAME = ""
PASSWORD = ""
SERVICE_NAME = "segmentation-service"
VIDEO_URL = "https://raw.githubusercontent.com/vicente87/segmentation-video-api/main/video_example/113-corneja-YouTube.mp4"

# Threshold parameters and paths (equivalent to subflow environment variables)
AUDIO_THRESHOLD = 0.4
FRAME_THRESHOLD = 0.2
RESULT_DIR = "./JSON-Result"
os.makedirs(RESULT_DIR, exist_ok=True)

# Global variables for state control (simulating Node-RED global.get/set)
global_state = {
    "list": 0,
    "list_f": 0,
    "num": 0,
    "num_frame": 0,
    "frame": 0,
    "num_bird": 0,
    "total_bird": 0,
}

def main():
  print("1. Downloading sample video...")
  response = requests.get(VIDEO_URL)
  if response.status_code != 200:
    print("Error downloading video.")
    return

  video_data = response.content
  video_filename = "113-corneja-YouTube.mp4"
  with open(video_filename, "wb") as f:
    f.write(video_data)

  print("2. Querying OSCAR API to retrieve MinIO credentials...")
  auth_str = f"{USERNAME}:{PASSWORD}"
  encoded_auth = base64.b64encode(auth_str.encode("ascii")).decode("ascii")
  headers = {"Authorization": f"Basic {encoded_auth}"}

  service_url = f"{OSCAR_SERVER}/system/services/{SERVICE_NAME}"
  res = requests.get(service_url, headers=headers)
  if res.status_code != 200:
    print(f"Error connecting to OSCAR: {res.status_code}")
    return

  service_info = res.json()
  bucket_input = service_info["input"][0]["path"]
  # bucket_name is extracted from the input bucket path (e.g., bucket/folder)
  bucket_name = bucket_input.split("/")[0]

  # Obtain MinIO configuration from service providers
  # Note: Depending on OSCAR structure, endpoint and credentials are extracted
  minio_endpoint = (
      service_info.get("storage_providers", {})
      .get("minio", {})
      .get("default", {})
      .get("endpoint", "")
  )
  # Clean endpoint of http:// or https://
  minio_endpoint = (
      minio_endpoint.replace("https://", "").replace("http://", "").strip("/")
  )
  access_key = service_info.get("storage_providers", {}).get("minio", {}).get("default", {}).get("access_key", "")
  secret_key = service_info.get("storage_providers", {}).get("minio", {}).get("default", {}).get("secret_key", "")

  print("3. Uploading video to MinIO bucket...")
  # Initialize MinIO client
  client = Minio(
      minio_endpoint,
      access_key=access_key,
      secret_key=secret_key,
      secure=True,
  )

  object_name = f"{bucket_input.split('/', 1)[1]}/{video_filename}"
  client.fput_object(bucket_name, object_name, video_filename)
  print("Video uploaded and service started successfully!")

  print("4. Connecting to MQTT broker to listen for events...")
  # MQTT client configuration (emqx broker)
  mqtt_client = mqtt.Client()
  mqtt_client.on_connect = on_connect
  mqtt_client.on_message = on_message

  mqtt_client.connect("broker.emqx.io", 1883, 60)
  mqtt_client.loop_forever()


def on_connect(client, userdata, flags, rc):
  print(f"Connected to MQTT broker with result code {rc}")
  # Subscription to the three main flow topics
  client.subscribe("segmentation-service/part")
  client.subscribe("audio-service/data")
  client.subscribe("frame-service/data")

def on_message(client, userdata, msg):
  topic = msg.topic
  payload = msg.payload.decode("utf-8")

  # --- Topic 1: Segmentation parts ---
  if topic == "segmentation-service/part":
    try:
      num_object = int(payload)
      global_state["list"] = num_object
      global_state["list_f"] = num_object
      global_state["num"] = 0
      global_state["num_frame"] = 0
      print(f"[Segmentation] Total parts to process: {num_object}")
    except ValueError:
      pass

  # --- Topic 2: Audio classification ---
  elif topic == "audio-service/data":
    process_audio_service(payload)

  # --- Topic 3: Object detection in frames ---
  elif topic == "frame-service/data":
    process_frame_service(payload)

def process_audio_service(data_str):
  i = global_state["num"]
  list_total = global_state["list"]
  num_bird = global_state["num_bird"]

  if list_total > i:
    try:
      # Logic equivalent to the 'object data' function node in Audio-Service
      prob_start = data_str.find("'probabilities': [") + 18
      prob_end = data_str.find("], 'labels_info':")
      prob_part = data_str[prob_start:prob_end]
      array_prob = [float(x.strip()) for x in prob_part.split(",")]

      label_start = data_str.find("'labels': [") + 11
      label_end = data_str.find("], 'probabilities':")
      label_part = data_str[label_start:label_end]
      array_label = [x.strip().strip("'\"") for x in label_part.split(",")]

      a = array_prob[0]
      aa = array_label[0]

      bird_detection = "No birds detection"
      if AUDIO_THRESHOLD <= a:
        bird_detection = aa
        num_bird += 1
        global_state["num_bird"] = num_bird

      result_dict = {
          "bird_detection": bird_detection,
          "probabilities": array_prob[:5],
          "labels": array_label[:5],
      }

      i += 1
      global_state["num"] = i
      process_msg = (
          f"{i} of {list_total} processes ( {num_bird} birds detected )"
      )
      print(f"[Audio Service] {process_msg} -> {result_dict}")

      # Save to file (equivalent to Node-RED file node)
      filename = os.path.join(RESULT_DIR, "result.json")
      with open(filename, "a") as f:
        f.write(json.dumps(result_dict) + "\n")

    except Exception as e:
      print(f"Error processing audio: {e}")

  if i == list_total:
    global_state["list"] = 0
    global_state["bird"] = 1
    global_state["num_bird"] = 0

def process_frame_service(data_str):
  i = global_state["num_frame"]
  list_total = global_state["list_f"]
  total_bird = global_state["total_bird"]

  if list_total > i:
    try:
      # Logic equivalent to the Frame-Service subflow
      # Expected format: object@prob1,prob2,...
      if "@" in data_str:
        obj_part, prob_part = data_str.split("@", 1)
      else:
        return

      array_prob = prob_part.split(",")
      i += 1
      global_state["num_frame"] = i

      bird_count = 0
      for item in array_prob:
        if ":" in item:
          _, thresh_str = item.split(":", 1)
          if "bird" in item.lower() and float(thresh_str) > FRAME_THRESHOLD:
            bird_count += 1
            total_bird += 1

      global_state["total_bird"] = total_bird

      payload_res = {
          "objectName": f"out_image/{os.path.basename(obj_part)}.jpeg",
          "bird_detection": f"{bird_count} birds detection",
          "object_detection": array_prob,
      }

      process_msg = f"{i} of {list_total} processes ( {total_bird} birds detected )"
      print(f"[Frame Service] {process_msg}")

      filename = os.path.join(RESULT_DIR, "frame_mqtt.json")
      with open(filename, "a") as f:
        f.write(json.dumps(payload_res) + "\n")

    except Exception as e:
      print(f"Error processing frame: {e}")

  if i == list_total:
    global_state["list_f"] = 0
    global_state["num_frame"] = 0
    global_state["frame"] = 1
    global_state["total_bird"] = 0

if __name__ == "__main__":
  main()
