The OSCAR Cowsay Service node shows the basic functionality for invoking the OSCAR service synchronously.

``` npm install node-red-contrib-oscar-cowsay-service```

Cowsay is a program that generates ASCII art pictures of a cow with a message.It can also generate pictures using pre-made images of other animals, such as Tux the Penguin, the Linux mascot.

# About Cowsay Service in OSCAR

The OSCAR Cowsay Service node shows the basic functionality for invoking the OSCAR service synchronously.

The invocation of the cowsay service in OSCAR can be seen in the following link:

## Inputs

The input variables will be the basic variables (OSCAR server url and credentials). In addition to the name that has been given to the cowsay service on the server. Inside the input msg.payload must be the text to write. With all these elements, the service token is searched and then a request is made to the service ( POST /run/{serviceName})

``` Syns```

## Outputs

Node returns in msg.payload an image like the one shown.

```                -------
                       \   ^__^
                        \  (oo)\_______
                           (__)\       )\/\
                               ||----w |
                               ||     || 
```

GRyCAP (Grupo de Grid y Computación de Altas Prestaciones) - UPV 