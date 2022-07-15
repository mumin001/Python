# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:13:08 2022

@author: User
"""

import random
n=100
numbers = list(range(1,n+1))
x = numbers.pop(random.randint(1,n+1))
print(x)

# x ni toping
# numbers2 = list(range(1,n+1))
# print(sum(numbers2)-sum(numbers))

summa = n*(n+1)/2
print(summa - sum(numbers))