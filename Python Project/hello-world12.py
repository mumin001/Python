# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:13:10 2022

@author: User
"""

# uquvchi_0 = {
#     'ism':'alijon',
#     'familiya':'suvanov',
#     'yosh':15,
#     'fakulted':'beyoqim',
#     'sinif':9
#     }

# print(uquvchi_0.items())

# for key, value in uquvchi_0.items():
#     print(f"kalit: {key}")
#     print(f"qiymat: {value} \n")

telefonlar = {
    'Ali':'iphone x',
    'Vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl',
    'Ali':'iphone x',
    'Vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl'
    }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
     }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
#         for buyum in bozorlik:
#             if buyum not in mahsulotlar:
#                 print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(telefonlar.values())

print('Foydalanuvchilar quydagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)
    
print('Foydalanuvchilar quydagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
    
    toys = {"ball", "car", "lamp", "ball", "bear", "car"}