#!/usr/bin/env python3

import json
import sys

BASE_URL = 'https://jitsi.binary-kitchen.de/'

if len(sys.argv) < 2:
    print('Give one ore more map files')
    exit(1)

for filename in sys.argv[1:]:
    js = json.load(open(filename))

    print('Jitsi rooms in', filename)
    for layer in js['layers']:
        if 'properties' in layer:
            for props in layer['properties']:
                if 'name' in props and props['name']=='jitsiRoom':
                    print(props['value'], BASE_URL+props['value'])
