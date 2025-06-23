![FlowFuse Logo](https://raw.githubusercontent.com/ai4os/ai4-compose/main/img/ff-logo--wordmark--light.png) 

# NodeRED-based solution

This repository contains a collection of nodes and interaction flows for [Node-RED](https://nodered.org/) specifically designed to interact with OSCAR. It includes example workflows, reusable subflows, and a Dockerfile for deploying a pre-configured Node-RED instance with all necessary dependencies.

## Available Modules

You can find all the custom OSCAR-related nodes grouped in the following collection:  
👉 [https://flows.nodered.org/collection/vAqHyycWgCq_](https://flows.nodered.org/collection/vAqHyycWgCq_)

Here’s a brief description of each:

- **OSCAR-bodypose-async**  
  Body Pose Detection using DEEP-Hybrid-DataCloud's pre-trained model.  
  [View in Marketplace](https://marketplace.deep-hybrid-datacloud.eu/modules/deep-oc-posenet-tf.html)

- **OSCAR-fish-detector-async**  
  Fish detection and classification based on YOLOv8, provided by OBSEA.  
  [View in Marketplace](https://dashboard.cloud.ai4eosc.eu/catalog/modules/obsea-fish-detection)

- **OSCAR-fish-detector-zip-async**  
  Same as fish-detector-async, but allows uploading multiple compressed images in a zip file.

- **OSCAR-litter-assessment-async**  
  Detects and quantifies plastic waste on water surfaces using a deep learning model.  
  [View in Marketplace](https://marketplace.deep-hybrid-datacloud.eu/modules/uc-cleluschko-deep-oc-litter-assessment-service.html)

- **OSCAR-phytonplankton-classifier-async**  
  Classifies phytoplankton species using a model provided by VLIZ.  
  [View in Marketplace](https://marketplace.deep-hybrid-datacloud.eu/modules/deep-oc-phytoplankton-classification-tf.html)

- **OSCAR-yolo**  
  Real-time object detection using the YOLOv8 model.  
  [View in Marketplace](https://marketplace.deep-hybrid-datacloud.eu/modules/deep-oc-yolov8-api.html)

- **OSCAR-plants-classification**  
  Classifies plant species using a synchronous pre-trained model.  
  [View in Marketplace](https://marketplace.deep-hybrid-datacloud.eu/modules/deep-oc-plants-classification-tf.html)

- **OSCAR-grayify**  
  Converts images to grayscale using ImageMagick.

- **OSCAR-cowsay**  
  Demonstration node that outputs text through the classic "cowsay" ASCII art.

---

## Getting Started

To run the modules or workflows (examples) locally, you must install the following Node-RED dependencies:

### OSCAR modules dependencies:

```bash
npm install node-red-contrib-string
npm install node-red-node-base64
```

### Workflow example dependencies:

```bash
npm install node-red-contrib-time_interval
npm install node-red-contrib-image-output
npm install node-red-contrib-exec-queue
npm install node-red-contrib-minio-all
npm install node-red-dashboard
npm install node-red-contrib-play-audio
```

---

## Using FlowFuse on AI4EOSC

If you have access to the AI4EOSC Flows infrastructure, you can use Node-RED directly through FlowFuse without installing anything locally.

Simply register or log in at:  
👉 [https://forge.flows.dev.ai4eosc.eu/](https://forge.flows.dev.ai4eosc.eu/)

You will have access to a ready-to-use Node-RED instance with OSCAR integration.

---

## Workflows and Examples

Explore the `examples` directory for complete workflows using the Node-RED dashboard to orchestrate services provided by OSCAR. These examples are a great starting point if you're new to the platform.

---

## Modules

The `modules` directory contains reusable components in JSON format. These can be imported directly into Node-RED.

---

## Documentation

To understand how to build and deploy pipelines with Node-RED in the AI4EOSC environment, visit:  
👉 [https://docs.ai4os.eu/en/latest/howtos/pipelines/flowfuse.html](https://docs.ai4os.eu/en/latest/howtos/pipelines/flowfuse.html)

---

*Feel free to contribute or provide feedback to help improve this repository!*
