# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 01:58:18 2022

@author: User
"""

from pprint import pprint
import json

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

# pprint(bemor)
# pprint(bemor)

import requests

r = requests.get("https://api.github.com")

pprint(r.json()) 