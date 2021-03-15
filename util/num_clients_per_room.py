#!/usr/bin/env python3

from urllib.request import urlopen

PUSHER_URL = "https://pusher.wa.binary-kitchen.de"
ROOM_PREFIX = "_/global/das-labor.github.io/workadv_das-labor"
METRICS_URL = PUSHER_URL + "/metrics"
NUM_CLIENTS_MARKER = 'workadventure_nb_clients_per_room'

with urlopen(METRICS_URL) as f:
    lines = f.readlines()

print('Number of clients per room in', ROOM_PREFIX)
for line in lines:
    line_str = line.decode()
    if NUM_CLIENTS_MARKER in line_str and \
        ROOM_PREFIX in line_str:

        # line of format
        # workadventure_nb_clients_per_room{room="_/global/das-labor.github.io/workadv_das-labor/main.json"} 20
        num = int(line_str.split('} ')[1])
        room = line_str.split(ROOM_PREFIX)[1].split('.json')[0]

        print(num, "in", room)
