# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 11:27:06 2022

@author: User
"""

# son = -72
# if son<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

# yosh = int(input('Yoshingiz nichida? '))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000
    
#     print(f"Sizga kirish {narh} so'm")

# kun = input("bugun kin nima?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("bugun kin nima?>>>")
# harorat = float(input("Havo xarorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("CHo'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("uyda dam olamiz!")
    
# kun = input("bugun kin nima?>>>")
# harorat = float(input("Havo xarorati qanday?"))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("CHo'milgani ketdik!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz!")  

# narh = 15000
# choy = True
# salat = True

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm") 

# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
    
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh + 5000
    
# if non:
#     print("Mijoz non oldi ")
#     narh = narh + 2000
    
# if kompot:
#     print("Mijoz kompot oldi ")
#     narh =narh + 5000
    
# if assorti:
#     print("Mijoz assorti oldi ")
#     narh = narh + 15000
    
#     print(f"Jami {narh} so'm")

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyrtma qabul qilindi.')
# else:
#     print('Avsuskiy bizda bunday ovqat yo\'q')

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz menuda {taom} yo'q")
    else:
        print("Savatchangiz bo'sh!")
        