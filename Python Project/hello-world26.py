# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:47:13 2022

@author: User
"""

from argparse import MetavarTypeHelpFormatter
from urllib.request import FancyURLopener


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1


def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
        
def update_bosqich(self):
        """Talabaning bosqichini 1taga kupaytirish"""
        self.bosqich += 1
        
def get_info(self):
        """Talaba xaqida malumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya


def get_age(self,yil):
        return yil - self.tyil
    
talaba1 = Talaba("olim", "Olimov", "2000")
talaba2 = Talaba("Xasan", "Xusanov", "1995")
talaba3 = Talaba("Akbar", "Alimov", "2004")
    
class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self,talabalar_son = 0
        self,talabalar = []
        
    def add_student(self,talaba):
        """Fanga talabalar qushish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilga talabalar haqida malumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni

def see_methods(klass):
   return [method for method in dir(klass) if method.startswith('__') is False]
print(see_methods(Talaba))
   
Matematika = Fan("Oliy Matimatika")
talaba1 = Talaba("Alijon", "Valiyev", "2000")
talaba2 = Talaba("Xasan", "Alimov", "2001")
talaba3 = Talaba("Akbar", "Boriyev", "2001")
Matematika.add_student(talaba1)
Matematika.add_student(talaba2)
Matematika.add_student(talaba3)

