# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:53:52 2022

@author: User
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# # ikki so'z 'ortasida o'xshashlik foizini topish
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))

# Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
# text = "салом"
# matches = process.extract(text, words, limit=3)
# print(matches)

# # Matnlar orasidan eng o'xshashini topish
text = "талба"
match = process.extractOne(text, words)
print(match)