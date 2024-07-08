
# Plant Classification Theano

Classify plant images among 10K species from the iNaturalist dataset.

## Installation

```bash
npm install node-red-contrib-oscar-plants-classification-theano
```

## About Plants

Classify plant images among 10K species from the iNaturalist dataset.

[Plants species classifier](https://dashboard.cloud.ai4eosc.eu/marketplace/modules/plants-classification)

## About Plants Service in OSCAR

This example uses the pre-trained classification model by DEEP-Hybrid-DataCloud Plants species classifier and is prepared to be used with synchronous invocations.

For more information consult:

[Plants Service](https://github.com/grycap/oscar/tree/master/examples/plant-classification-yolo-sync)

## Inputs

The input variables will be the basic variables (OSCAR server URL and credentials). In addition to the name that has been given to the plants service on the server. Inside the input `msg.payload` must be the image data to classify. With all these elements, the service token is searched and then a request is made to the service (`POST /run/{serviceName}`).

[API Documentation](https://docs.oscar.grycap.net/api/)

## Outputs

The node returns through `msg.payload` plant classification data using Tensorflow.

---

Grupo de Grid y Computación de Altas Prestaciones (GRyCAP) - Universitat Politècnica de València (UPV)
