# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:17:54 2019

@author: Python
"""
import random

fjarsjodur = random.randint(1,4)
kista1 = random.randint(2,4)
kista2 = random.randint(2,4)

while kista1 == fjarsjodur:
    kista1 = random.randint(2,4)
print("Kista",kista1,"var fjarlægð")

while kista2 == fjarsjodur or kista2 == kista1:
    kista2 == random.randint(2,4)
print("Kista",kista2,"var fjarlægð")
    
print("Kista nr.",fjarsjodur,"inniheldur fjarsjóðinn")
if fjarsjodur == 1:
    print("Þú fannst fjársjóðinn!")
else:
    print("Þú fannst ekki fjársjóðinn!")