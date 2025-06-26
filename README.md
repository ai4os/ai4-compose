<div align="center">
  <img src="https://github.com/ai4os/ai4-compose/blob/main/img/ai4compose-logo-transparent.png" alt="ai4compose architecture" width="500"/>
</div>

# AI4Compose

AI4Compose is a suite of software utilities designed to facilitate the integration and orchestration of multiple artificial intelligence (AI) models and machine learning techniques. Its primary function is to amalgamate various AI components into organised workflows or pipelines. AI4Compose integrates with well-known visual programming tools such as [Elyra](https://github.com/elyra-ai/elyra) and [Node-RED](https://nodered.org/) (along with [FlowFuse](https://flowfuse.com/), enabling the creation of workflows from the inference of pre-trained models. Users can work with nodes and connections between them. Despite their different functionalities and capabilities, both platforms share a common purpose in utilising graphical composition tools applicable to AI models. As a tool for executing inference tasks, AI4Compose has been integrated with [OSCAR](https://oscar.grycap.net/). 

<div align="center">
  <img src="https://github.com/ai4os/ai4-compose/blob/main/img/Runtime_view_AI4Compose.png" alt="ai4compose architecture" width="500"/>
</div>

## Elyra Integration

In Elyra, AI4Compose presents a series of notebooks utilising OSCAR's functionalities, integrating OSCAR's Python client to invoke and interact with OSCAR services. This integration facilitates users in seamlessly blending AI models and machine learning techniques into their data science workflows, leveraging Elyra's notebook-based environment for a more efficient and productive development experience.

## Node-RED Integration

For Node-RED, AI4Compose introduces new modules based on subflows. These subflows efficiently employ standard Node-RED nodes to make requests to OSCAR services. Users can effortlessly interact with these modules in a graphical environment through a "drag and drop" interface, enabling them to compose complex workflows with ease. You can also visit the list of published nodes and subflows in the [Node-RED Library](https://flows.nodered.org/collection/pTY6eq8gA0Q5).

In both platforms, AI4Compose stands as a testament to the innovative fusion of AI orchestration and visual programming, offering users an accessible and powerful toolset for developing sophisticated AI-powered applications.

## More info and tutorials
You can obtain more info of AI4Compose in the [official documentation of the AI4EOSC Project](https://docs.ai4os.eu/en/latest/howtos/pipelines/index.html). Also, you can find demo tutorials in the AI4EOSC [Youtube](https://www.youtube.com/@ai4eosc) channel.


[![SQAaaS badge shields.io](https://img.shields.io/badge/sqaaas%20software-silver-lightgrey)](https://api.eu.badgr.io/public/assertions/mmlz4p1eTvi5-ZEwXSpUdA "SQAaaS silver badge achieved")

<div align="center">
  <img src="https://ai4eosc.eu/wp-content/uploads/sites/10/2022/09/horizontal-transparent.png" alt="logo" width="500"/>
</div>

## Acknowledgements

<img width=300 align="left" src="https://raw.githubusercontent.com/AI4EOSC/.github/ai4eosc/profile/EN-Funded.jpg" alt="Funded by the European Union" />

This project has received funding from the European Union’s Horizon Research and Innovation programme under Grant agreement No. 101058593
