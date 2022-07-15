# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:30:26 2022

@author: User
"""

# def toliq_ism_yasa(ism, familiya):
#     """Toliq isim qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
    
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"darsga kilmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib kildi")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isim qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov', 'abrorovich')
# print(f"darsga kilmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
print("Sayitimizdagi avtolar ro'yxatini shakillantiramiz.")
avtolor=[]
while True:
    print("\nQuydagi malumotlarni kiriting ", end='')
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yil, narhi))
    
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
    
print("\nSalonimiz dagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")

# avto1 = avto_info('GM','Malibu','Qora','Avtomat','2018')
# avto2 = avto_info('GM', 'Oq','Mehanika',2016,15000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud avto mashinalar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto}['rang']} {avto['model']}.Narh: {narh}")

# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#         return sonlar
    
# print(oraliq(0,10))
# print(oraliq(10,20))
 
