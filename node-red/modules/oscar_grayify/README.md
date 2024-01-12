This node supports highly-scalable event-driven image conversion to grayscale using the popular ImageMagick software.

```npm install node-red-contrib-oscar-grayify```

# About Grayify

This node supports highly-scalable event-driven image conversion to grayscale using the popular ImageMagick software.

ImageMagick® is a free and open-source software suite for displaying, converting, and editing raster image and vector image files. It can read and write over 200 image file formats, and can support a wide range of image manipulation operations, such as resizing, cropping, and color correction.

[ImageMagick](https://imagemagick.org/index.php)

# About Grayify Service in OSCAR

The goal of this service is to have:

An input bucket created in Minio on which the user uploads the files to be converted.
A function that is triggered upon each file upload in order to trigger the file conversion, which is automatically handled by an elastic Kubernetes cluster that provisions additional nodes on-demand if required.
An output bucket created in Minio on which the user will find the converted files.

For more information consult:

[Grayify Service](https://github.com/grycap/oscar/tree/master/examples/imagemagick)

## Inputs

The input variables will be the basic variables (OSCAR server url and credentials). In addition to the name that has been given to the grayify service on the server. Inside the input msg.payload must be the text to write. With all these elements, the service token is searched and then a request is made to the service ( POST /run/{serviceName}).

```Syns```

## Outputs

The node returns through msg.payload the grayscale image (base64), which can be used in image display nodes such as images preview node. GRyCAP (Grupo de Grid y Computación de Altas Prestaciones) - UPV 