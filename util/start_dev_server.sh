#!/usr/bin/bash

PORT=8009

# starting http server
cd $(dirname $0)/.. 
python3 util/no_cors_server.py $PORT &
# using ngrok to relay
ngrok http $PORT

