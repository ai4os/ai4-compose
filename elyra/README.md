# ![Elyra Logo](https://raw.githubusercontent.com/ai4os/ai4-compose/main/img/elyra-horizontal-color.svg) Elyra-based solution

This repository contains examples of how to use [OSCAR](https://oscar.egi.eu) with Elyra to create and manage AI pipelines in JupyterLab. It includes ready-to-use components that demonstrate the capabilities of Elyra and OSCAR in the context of AI workflows.

## Available Nodes

These are the nodes currently included in this repository. Each one can be deployed as a service in OSCAR using its corresponding container image:

- **Cowsay**  
  A fun demonstration node that makes a cow say the input text provided via environment variable.  
  Docker image: `ghcr.io/grycap/cowsay:latest`

- **Grayify**  
  Converts an input image to grayscale. Useful for preprocessing tasks in computer vision workflows.  
  Docker image: `ghcr.io/grycap/imagemagick:latest`

- **Plant Classification**  
  A classification node that takes an image of a plant and predicts its species using a trained model.  
  Docker image: `ai4oshub/plants-classification`

- **YOLOv8 Inference**  
  Performs object detection on input images using a YOLOv8 model. Ideal for detecting objects in real-time data pipelines.  
  Docker image: `ai4oshub/ai4os-yolov8-torch`

---

## Installation

If Elyra is not yet installed on your JupyterLab, you can install it by following these steps:

1. Open your terminal.
2. Install Elyra using pip:

```bash
pip install elyra && jupyter lab build
```

### Installation of Elyra with All Extensions

For a comprehensive installation of Elyra with all its extensions in the latest version, please review the official Elyra documentation at:  
https://elyra.readthedocs.io/en/latest/getting_started/installation.html

The command to install Elyra with all extensions is:

```bash
pip3 install --upgrade "elyra[all]"
```

This will ensure that you have all the necessary extensions to fully utilize the capabilities of Elyra.

3. If necessary, restart JupyterLab.

---

## Using Elyra on EGI Notebooks

If you are a member of a [Virtual Organization (VO)](https://www.egi.eu/virtual-organisations/) within the EGI infrastructure, you can use Elyra directly without installing anything locally. Simply log in to:

👉 [https://notebooks.egi.eu/](https://notebooks.egi.eu/)

Once logged in, you’ll have access to a JupyterLab environment that includes Elyra.

---

## Starting JupyterLab Locally

To start JupyterLab on your machine:

1. Open your terminal.
2. Navigate to your project directory:

```bash
cd /path/to/your/project
```

3. Start JupyterLab by running:

```bash
jupyter lab
```

A new browser window or tab should open with JupyterLab.

---

## Using the Examples

Once JupyterLab is running, navigate to the `examples` folder. There, you will find complete pipeline examples and individual components. These serve as templates to help you build your own pipelines using Elyra and OSCAR.

Take advantage of Elyra’s graphical pipeline editor to visually compose, configure, and run your workflows.

To better understand how Elyra pipelines work within AI4EOSC, consult the official guide:  
👉 [https://docs.ai4os.eu/en/latest/howtos/pipelines/elyra.html](https://docs.ai4os.eu/en/latest/howtos/pipelines/elyra.html)

---

*This is a work in progress. Please feel free to contribute or provide feedback!*
