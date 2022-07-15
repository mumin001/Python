# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 01:00:41 2022

@author: User
"""

import datetime as dt

hozir = dt.datetime.now()
# print(hozir)

# print(hozir.hour)

# print(hozir.minute)

# print(hozir.second)

# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2022,7,16)
# print(f"Ertangi sana: {ertaga}")

# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqrHozir}")
# vaqtKeyin = dt.time(11,1,00)
# print(vaqtKeyin)

# bugun = dt.date.today()
# ramazon = dt.date(2022,7,17)
# farq = ramazon-bugun
# print(farq)
# print(f"Ramazonga {farq.days} kun qoldi")

hozir = dt.datetime.now()
futbol = dt.datetime(2022, 7, 20, 00, 00, 00)
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar / 60)
soatlar = int(minutlar / 60)
print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi")

vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)