# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:06:23 2022

@author: User
"""

from avto import Avto

avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 1000)
avto1 = Avto("GM", "Lasetti", "Oq", 2020, 20000, 1000)
avto3 = Avto("Tyota", "Carolla", "Silver", 2020, 35000,1000)
print(Avto.get_num_avto())