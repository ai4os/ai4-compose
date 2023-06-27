# Elyra-based solution

This repository contains examples of how to use OSCAR with Elyra.

## Installation
If Elyra is not yet installed on your JupyterLab, you can install it by following these steps:

1. Open your terminal.
2. Install Elyra using pip:

```bash
pip install elyra && jupyter lab build
```

## Installation of Elyra with All Extensions

For a comprehensive installation of Elyra with all its extensions in the latest version, please review the official Elyra documentation available at: https://elyra.readthedocs.io/en/latest/getting_started/installation.html. 

The command to install Elyra under these conditions is as follows:

```bash
pip3 install --upgrade "elyra[all]"
```

This will ensure that you have all the necessary extensions to fully utilize the capabilities of Elyra.

3. If necessary, restart JupyterLab.

## Starting JupyterLab

To start JupyterLab, follow these steps:

1. Open your terminal.
2. Navigate to your project directory:

```bash
cd /path/to/your/project
```

3. Start JupyterLab by running the following command:

```bash
jupyter lab
```

A new browser window or tab should open with JupyterLab.

## Using the Examples

Once you have JupyterLab opened, navigate to the `examples` folder. There, you will find complete pipeline examples as well as individual components. Use these examples as templates or guides to help you build your own pipelines using OSCAR and Elyra.

Remember, Elyra provides an intuitive graphical interface for building your pipelines. So take advantage of this functionality as you work with the example pipelines and components.
