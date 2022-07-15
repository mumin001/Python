# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:31:21 2022

@author: User
"""

with open("pi.txt") as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = float(pi)
print(pi)


filename = "data/talabalar.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)