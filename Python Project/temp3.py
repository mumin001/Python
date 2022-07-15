# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:39:02 2022

@author: User
"""

# pip install googletrans==3.1.0a0
from googletrans import Translator

tarjimon = Translator()

msg = 'Tarjima uchun suz kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)