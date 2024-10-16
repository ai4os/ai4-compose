# Object Detection with YOLOv8

Detect objects in images using the state-of-the-art YOLOv8 model.

## Installation

To install the module, use the following command:

```bash
npm install node-red-contrib-oscar-yolo
```

## About YOLO

This node utilizes the YOLOv8 (You Only Look Once version 8) model to detect objects within images. YOLOv8 is a cutting-edge, real-time object detection system known for its speed and accuracy, capable of identifying thousands of object categories efficiently.

[YOLOV8 model](https://dashboard.cloud.ai4eosc.eu/marketplace/modules/ai4os-yolov8-torch)

## About YOLOV8 Service in OSCAR

his service uses the pre-trained YOLOv8 model provided by DEEP-Hybrid-DataCloud for object detection. It is designed to handle synchronous invocations and real-time image processing with high scalability, managed automatically by an elastic Kubernetes cluster.

For more information consult:

[YOLOV8](https://github.com/ai4os-hub/ai4os-yolov8-torch)

## Inputs

The input variables will be the basic variables (OSCAR server URL and credentials). In addition to the name that has been given to the YOLO service on the server. Inside the input `msg.payload` must be the image data to classify. With all these elements, the service token is searched and then a request is made to the service (`POST /run/{serviceName}`).

[API Documentation](https://docs.oscar.grycap.net/api/)

## Outputs

These results can be visualized using compatible nodes, such as image preview nodes, to see the detected objects directly on the images.


---

Grupo de Grid y Computación de Altas Prestaciones (GRyCAP) - Universitat Politècnica de València (UPV)
