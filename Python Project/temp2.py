# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# pip install googletrans==3.1.0a0
from googletrans import Translator
tarjimon = Translator()

matn_uz = "Paython - dunyodagi eng mashhur dasturlash tili"

tarjima = tarjimon.translate(matn_uz)

# print(tarjima.orgin)

# print(tarjima.text)

# print(tarjima.src)

tarjima_ru = tarjimon.traslate(matn_uz, dest='ru')
# print(tarjima_ru.text)

matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en,dest='uz')
print(tarjima_uz.text)

