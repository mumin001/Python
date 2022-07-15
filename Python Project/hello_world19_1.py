# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:55:24 2022

@author: User
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narh=None):
    """Avtomobil haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto



def avto_kirit():
    """Foydalanuchiga avto_info funksiyasi yordamida bir nishta avtolar haqida ma'lumotlarni bitta"""
    avtolar=[]
    while True:
        print("\nQuydagi malumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Model: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        javob = input("Yana avto qushasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar



def info_print(avto_info):
    """Avtomobillar haqida malumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['koronka']} korobka,"
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")