# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:54:21 2022

@author: User
"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
        baholar[ism]=int(baho)
    return baholar
talabalar = ['ali', 'vali', 'xasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)