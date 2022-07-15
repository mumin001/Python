# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 15:24:58 2022

@author: User
"""

# car_0 = {'model': 'ferrari', 'rang': 'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

en_uz = {'apple': 'olma', 'apricot': 'o\'rik', 'banana': 'banan'}

# mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so'm")

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tug'ulgan,\
#  {talaba_0['yosh']} yoshda")
 
# talaba_0['kurs'] = 4
# talaba_0['fakulted'] = 'informatika'
# talaba_0['ism'] = 'andulloh'

# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)

# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}

# del talaba_0['yosh']
# print(talaba_0)

telefonlar = {
    'Ali':'iphone x',
    'Vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'pixel 3xl'
    }

meva = en_uz.get('pineapple', 'Bunday meva mavjud emas')

phone = telefonlar.get('hasan')
print(phone)