# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:30:42 2022

@author: User
"""

import unittest
from hello_world33 import get_ful_name

class hello_world33_tets(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_ful_name('alijon', 'valiyev')
        self.assertEqual(name, 'Alijon Valiyev')
        
    def test_otasining_ismi(self):
        name = get_ful_name("alijon", "valiyev", "olimovich")
        self.assertEqual(name, 'Alijon Olimovich Valiyev')
        
unittest.main()