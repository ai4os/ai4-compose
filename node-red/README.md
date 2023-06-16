# NodeRED-based solution
In this folder, nodes and interaction flows of NodeRED (https://nodered.org/) with OSCAR are located. In addition to the examples of workflows.

To run the subflows (nodes) or workflows (examples), it is necessary to install the following nodes (dependencies) for everything to work correctly.


## Getting Started

In this repository, you will find a collection of nodes and interaction flows for NodeRED (https://nodered.org/) specifically designed to interact with OSCAR. This includes examples of workflows, subflows, and a Dockerfile that prepares a Node-RED image with all the required dependencies installed.


To run the subflows (nodes) or workflows (examples), you must first install the necessary dependencies:

OSCAR subflow :

     • node-red-contrib-string (npm install node-red-contrib-string)
     • node-red-node-base64 (npm install node-red-node-base64)

Example workflow execution:
      
     • node-red-contrib-time_interval (npm install node-red-contrib-time_interval)
     • node-red-contrib-image-output (npm install node-red-contrib-image-output)
     • node-red-contrib-exec-queue (npm install node-red-contrib-exec-queue)
     • node-red-contrib-minio-all (npm install node-red-contrib-minio-all)
     • node-red-dashboard (npm install node-red-dashboard)
     • node-red-contrib-play-audio (npm install node-red-contrib-play-audio) 

## Dockerfile

In the root of this repository, a Dockerfile is provided. This Dockerfile can be used to build a Docker image that includes a ready-to-use instance of Node-RED, preconfigured with all the necessary subflows to communicate with OSCAR.

To build the Docker image, use the following command:

```sh
docker build -t your_image_name .
```

## Workflows and Examples

A dedicated directory is provided where the workflows for each of the OSCAR services are located. This is coupled with examples of workflows where the Node-RED dashboard is used to choreograph OSCAR services. These are an excellent resource if you're new to OSCAR or wish to see some example implementations.

## Subflows

A separate folder contains all the subflows, which can be tested individually. These are JSON files that can be imported directly into your Node-RED instance for testing and development. 

Please feel free to use these as a starting point for creating your own, customised subflows.


