# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:55:24 2022

@author: User
"""

# import avto_info_lib

# avtolar = avto_info_lib.avto.kirit()

# for avto in avtolar:
#     avto_info_lib.info_print(avto)
# birinci funksiya
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
     """Avtomobil haqidagi malo'motlarni lug'at ko'rinishida qaytaro'vchi funksiya"""
     avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
     return avto
 
# print("Sayitimizdagi avtolar ro'yxatini shakillantiramiz.")
# ekinchi funksiya
def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nichta avtolar haqida malumotlarni bitta"""
    avtolor=[]
    while True:
        print("\nQuydagi malumotlarni kiriting ", end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
    
     avtolar.append(avto_kirit(kompaniya, model, rangi, korobka, yil, narhi))
    
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    return avtolar
    
# print("\nSalonimiz dagi avtolar:")
#  for avto in avtolar:
#    if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")