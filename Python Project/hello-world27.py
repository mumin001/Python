# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:45:30 2022

@author: User
"""

class Shaxs:
    """Shaxslar xaqida malumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ims = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ulgan"
        return info
    def get_age(self,yil):
        """Shaxisning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba kilasi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning uqish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
class Manzil:
    """Manzil saqlash uchun kilass"""
    def __init__(self,uy,kucha,tuman,viloyat):
        """Manzil hussiaytlari"""
        self.uy = uy
        self.kucha = kucha
        self.tuman = tuman
        self.viloyat =viloyat
        
    def get_manzil(self):
        """Manzilni kiritish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kucha} kuchasi, {self.uy} uy"
        return manzil

talaba1_manzil = Manzil(12,"Olmazor","Bogbod","Samarkand")
talaba1 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba1_manzil)