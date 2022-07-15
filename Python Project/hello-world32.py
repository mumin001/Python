# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:43:09 2022

@author: User
"""

yosh = input("Yoshingizni kiriting: ")

try:
    yosh = int(yosh)
    print(f"Siz {2022-yosh} yilda tug'ulgan siz")
except:
    print("Butun son kiritmadingiz")

print("Dastur tugadi")

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"Siz {2022-yosh} yilda tug'ulgan siz")