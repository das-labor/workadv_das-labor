#!/usr/bin/bash

PORT=8003
LOGFILE=$0.log

# starting http server
cd "$(dirname "$0")/.." || exit
python3 util/no_cors_server.py "$PORT" >> "$LOGFILE" 2>&1 &
P1="$!"

# using ngrok to relay
ngrok http "$PORT"

kill "$P1"

