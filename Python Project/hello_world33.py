# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 11:21:10 2022

@author: User
"""

def get_ful_name(ism,familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()
    else:
        return f"{ism} {familiya}".title()