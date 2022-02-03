#!/bin/bash
# Small script to run docker with the required params for this image to work
if [[ $(which docker) && $(docker --version) ]]; then
    docker run -it \
    --mount type=bind,source=$(pwd),target=/usr/src/html2pdf/input,bind-propagation=slave,ro \
    -v $(pwd):/usr/src/html2pdf/output \
    -u $(id -u):$(id -g) \
    ramonvd/pdfconvert:latest "$@"
else
    echo "No tens Docker instal·lat. Cal que l'instal·lis primer, seguint les instruccions a: https://docs.docker.com/engine/install/ubuntu/"
fi
