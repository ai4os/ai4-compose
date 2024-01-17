Classify plant images among 10K species from the iNaturalist dataset.

```npm install red-contrib-oscar-plants```

# About Plants

Classify plant images among 10K species from the iNaturalist dataset.

[Plants species classifier](https://marketplace.deep-hybrid-datacloud.eu/modules/deep-oc-plants-classification-tf.html)

# About Plants Service in OSCAR

This example uses the pre-trained classification model by DEEP-Hybrid-DataCloud Plants species classifier and is prepared to be used with synchronous invocations.

For more information consult:

[Plants Service](https://github.com/grycap/oscar/tree/master/examples/plant-classification-sync)

## Inputs

The input variables will be the basic variables (OSCAR server url and credentials). In addition to the name that has been given to the plants service on the server. Inside the input msg.payload must be the text to write. With all these elements, the service token is searched and then a request is made to the service ( POST /run/{serviceName}).

```Syns```

## Outputs

The node returns through msg.payload plant classification image using Lasagne/Theano (base64), which can be used in image display nodes such as images preview node. GRyCAP (Grupo de Grid y Computación de Altas Prestaciones) - UPV