# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 08:34:38 2022

@author: User
"""

# input()
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nichida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz nicha mert? ")
# height = float(height)

# while()
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son + 1
#     son += 1

# print('dastur tugadi')

# while in input
# print("Kiritilgan soning kivadiratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni tuxtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
        
# print("Dastur tugadi")

# ishora
# print("Kiritilgan soning kivadiratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni tuxtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora == 'Fasle'
#     else:
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi!')

# break while
# print("Kiritilgan soning kivadiratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni tuxtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi!')

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# CONTAINER
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# Continue while
# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)

# infinite loop
# son = 0
# while son<10:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)


son = 1
while son>0:
    son += 1
    if son%2==0:
        continue
    else:
        print(son)