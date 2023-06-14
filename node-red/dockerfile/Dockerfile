# Use official Node-RED image
FROM nodered/node-red

# Set the working directory in the Docker container
WORKDIR /usr/src/node-red

# Install additional Node-RED flows
RUN npm install node-red-contrib-string && \
    npm install node-red-node-base64 && \
    npm install node-red-contrib-time_interval && \
    npm install node-red-contrib-image-output && \
    npm install node-red-contrib-exec-queue && \
    npm install node-red-contrib-minio-all && \
    npm install node-red-dashboard && \
    npm install node-red-contrib-play-audio

# Install git to clone the repository
USER root
RUN apk update && \
    apk add git

# Clone the repository into the current directory
RUN git clone https://github.com/grycap/oscar_nodered.git

# Copy the custom flows to /data
COPY flows.json /data/flows.json

# Copy the custom settings to /data
COPY settings.js /data/settings.js

# Switch to the node-red user to run the service
USER node-red

# Specify that the container is listening on port 1880
EXPOSE 1880

# Run Node-RED
CMD ["npm", "start"]
