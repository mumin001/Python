# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 18:35:32 2022

@author: User
"""

from uuid import uuid4


class avto:
    """Avtomobil kilassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        avto.__num_avto += 1    
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
        
    def add_km(self,km):
        """Mashinaning km ga yana km qushish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bulmaydi")
