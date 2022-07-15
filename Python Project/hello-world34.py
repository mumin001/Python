# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:40:34 2022

@author: User
"""

import json
import googlemaps
from apiley import APIKEY

gmaps = googlemaps.Client(key=APIKEY)

geocode_result = gmaps.geocode('Olmazor','Tashkent','Uzbekistan')

g = json.dumps(data[0], indent = 4, sort_keys=True)
print(g)

data = data[0]
kenglik = data['geometry']["lokation"]['lat']
uzunlik = data['geometry']["lokation"]['lat']
print(f"{kenglik},{uzunlik}")