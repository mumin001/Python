# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:53:47 2022

@author: User
"""

import requests
from pprint import pprint

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
pprint(r.text)

country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
# print(r_json.keys())
print(r_json["capital"])