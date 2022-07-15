# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 09:39:36 2022

@author: User
"""

import unittest
from temp import Car

class CarTest(unittest.TestCase):
    """Car kilassini tekshirish uchun test"""
    def setup(self):
        make = 'GM'
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
        
    def test_create(self):
        
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model,self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        
        self.assertIsNotNone(self.avto1.price)
        
        self.assertEqual(0,self.avto1_get_km())
        
        self.assertEqual(self.price,self.avto2.price)
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
        
    def test_add_km(self):
        
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(5000,self.avto1.get_km())

        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
        
unittest.main()