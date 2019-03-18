# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:22:58 2019

@author: Python
"""

import random
def fjarsjodsleikur():

#Vel númer á fjársjóðskistu
    fjarsjodur = random.randint(1,4)

#Leikmaður velur sér kistu (í okkar tilfelli kistu nr.1)
    i = 1

#Leikmaður skiptir alltaf um kistu (þ.e. c=0)
#Niðurstöðu skilað, þ.e. hvort fjársjóðskistan hafi verið valin eða ekki
#Sigur breytan segir til um hvort leikmaður hafi sigrað eða ekki
    if fjarsjodur == i:
        sigur = 1
    else:
        sigur = 0

    return sigur

#Bý til breytu sem geymir fjölda sigra
sigrar = 0
 #Spila leikinn 1000 sinnum til að athuga hversu oft leikmaður fékk verðlaun
for j in range(1000):
    sigrar = sigrar + fjarsjodsleikur()

#Prenta út sigurhlutfall 1000 keyrsla.
print('Líkur á því að vinna til verðlauna eru:',sigrar/1000)