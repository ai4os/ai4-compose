## About this repository

In this repository, you will find the development of the article "Visual Composition of AI Inference Pipelines for the Compute Continuum". Below is a summary of the work developed, which can be seen at (article URL).

This paper introduces an architecture to achieve the visual composition of AI(Artificial Intelligence) inference pipelines and their execution along the compute continuum. It integrates the OSCAR event-driven data-processing serverless platform that runs on elastic Kubernetes clusters and on multiple computer architectures along the compute continuum. The visual composition of AI inference pipelines is achieved via Node-RED, a visual programming tool for wiring together devices, APIs, and online services, creating scalable and flexible Internet of Things (IoT) applications. Also, as a Python-based alternative, Elyra is supported, which streamlines machine learning workflows integrating seamlessly with Jupyter Notebooks for efficient and reproducible ML pipeline management. Support to custom nodes for OSCAR is integrated with both visual platforms, facilitating the composition of AI inference pipelines. The visual design of event-driven pipelines on the continuum is achieved via a Functions Definition Language (FDL) Composer tool, which defines the set of AI models deployed as services across multiple OSCAR clusters in the compute continuum. To assess the benefits of the proposed approach, a use case is designed to process wildlife video to simultaneously perform both animal detection and bird recognition from the audio, involving resources from the compute continuum.

## Videos examples  

In the videos directory, there are several examples of videos that could be used as examples.

## Node-RED example

In the root of the project, you will find the Node-RED `.json` file that contains the full example workflow developed in the article.

For proper execution, make sure the following nodes are installed:

- [`node-red-contrib-minio-all-fix`](https://www.npmjs.com/package/node-red-contrib-minio-all-fix)
- [`node-red-contrib-image-output`](https://www.npmjs.com/package/node-red-contrib-image-output)
