# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:06:37 2022

@author: User
"""

# x=10
# print(type(x))
# matn = "Salom"
# print(type(matn))
# print(matn.upper())
# print(x.upper())

# def salom():
#     print("Assalomu alaykum")

# print(type(salom))

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self,yil):
        return yil - self.tyil
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ulgan yilim {self.tyil}"

talaba1 = Talaba("olim", "Olimov", "2000")
talaba2 = Talaba("Xasan", "Xusanov", "1995")
talaba3 = Talaba("Akbar", "Alimov", "2004")