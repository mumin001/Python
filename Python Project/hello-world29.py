# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:53:55 2022

@author: User
"""

class Avto:
    """Avtomobil kilassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
        
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self,y):
        return self.narh==y.narh
    
    def __it__(self,y):
        return self.narh<y.narh
    
    def __le__(self,y):
        return self.narh<=y.narh
    
    
class AvtoSalon:
    """Avtosalon kilassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
        
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def __add__(self,boshqa_salon):
        if isinstance(y,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self,name} {y,name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon(y)
    
    def add_avto(self,*qiymat):
        if isinstance(Avto,Avto):
            self.avtolar.append(Avto)
        else:
            print("Avto kiriting")
    
salon1 = AvtoSalon("MaxAuto")
salon2 = AvtoSalon("Avto lider")
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("Tyota", "Carolla", "Silver", 2020, 35000)
avto3 = Avto("Mazda", "6", "Qizil",2015, 35000)
salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Volkswagen", "Polo", "Qora", 2015, 30000)
avto5 = Avto("Xonda", "Sanata", "Oq", 2017, 42000)
avto6 = Avto("KIA","K8", "Qora", 2022, 77777)
salon2(avto4,avto5,avto6)