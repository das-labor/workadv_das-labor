#!/usr/bin/bash

PORT=8003
LOGFILE=$0.log

# starting http server
cd $(dirname $0)/.. 
python3 util/no_cors_server.py $PORT 2>&1 >> $LOGFILE &

# using ngrok to relay
ngrok http $PORT

