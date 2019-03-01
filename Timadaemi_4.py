#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:35:09 2019

@author: nestIH
"""

# =============================================================================
# Tímadæmi4. Klasar og hlutir. Setja upphæð inn á bankareikning
# Einföld útgáfa af bankareikning klasa sem leggja á í sér skrá
# =============================================================================
class Bankareikningur():
    def __init__(self, inneign=0, str1= ' '):
        self.inneign= inneign
        self.str1= str1
        
    def leggja_inn(self,upphaed):
        if upphaed < 0:
            return False
        else: 
            self.inneign += upphaed
            if self.inneign >=0: return True
            else: return False
    
    def taka_ut(self, upphaed):
        self.inneign -= upphaed
        if self.inneign  >0:
            return True
        else:
            self.inneign += upphaed
            return False
        
    def saekja_stodu(self):
        if self.inneign < 0:
            raise ValueError('Neikvæð upphæð á reikningi')
        return self.inneign

def main():
    print('Main fallið var kallað')
if __name__ == '__main__':
    main()
else: 
    print('import hefur verið gert á klasanum')

# =============================================================================
# Hanna á þennan klasa í sér skrá
# from bankareikningur import Bankareikningur
# =============================================================================

class Bankavidskipti:
    def __init__(self, reikningur, str= ' '):
        self.reikningur= reikningur
        self.str= str
    
    def Inn_reikning(self):
        while(True):
            pass
            #Lesa inn upphæð í heiltölum sem setja á inn á reikning
            #Ekki má leggja inn neikvæða upphæð eða textatákn en notandi 
            #prufar þá aftur. Fallið kallar á "leggja_inn" og prentar út 
            #innlagða upphæð ef allt gekk vel
            #Prenta út villumeldingu ef ekki gekk að leggja inn.
            #Nota try: og except: við kall á "leggja_inn" fallið
            #Spyrja notanda hvort hann vilji leggja aftur inn
            #Nota stýrsegð til að komast út úr lykkjunni og fallinu 
            #t.d. með input('hætta=N')
            
    def takaUt_reikning(self):
        pass
    
    def saekjaStodu_reikning(self):
        pass
    
def main():
    reikningur= Bankareikningur()
    vskipti= Bankavidskipti(reikningur)
    vskipti.Inn_reikning()
    print('Innistæða á reikning er {0}'.format(reikningur.inneign))

if __name__ == '__main__':
    main() 
