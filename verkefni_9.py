#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# =============================================================================
# Created on Sat Oct 27 23:56:52 2018
# =============================================================================

@author: nestIH
"""
from bankareikningur import Bankareikningur
import pickle
class Bankavidskipti:
    def __init__(self, reikningur, str= ' ' ):
        self.reikningur= reikningur
        self.str= str
# =============================================================================
#     
# =============================================================================
    def Inn_reikning(self):
            while(True):
                self.str= input('Viltu leggja inn: Ja eða Nei?')
                if self.str =='Ja':
                    try:
                        upphaed= int(input('Sláðu inn upphæð í heiltölum:'))
                        try:
                            reikn_svar= self.reikningur.leggja_inn(upphaed)
                            if reikn_svar==True: print('Innlögð upphæð er {0}: '.format(upphaed))
                            elif reikn_svar==False and upphaed<0: print('Ekki hægt að leggja inn neikvæða upphæð!')
                            else: print('Villa kom upp innieign á reikning er neikvæð {0}:'.format(self.reikningur.inneign))
                        except:
                            print('Villa 1 kom upp')
                            break
                        self.str= input('Ný innsetning, N=Hættir?')
                        if self.str == 'N': 
                            return
                    except:
                        print('Villa  2 kom upp')
                        break
                elif self.str =='Nei': return
            self.Inn_reikning()
# =============================================================================
#         
# =============================================================================
    def takaUt_reikning(self):
        while(True):
                self.str= input('Viltu taka út: Ja eða Nei?')
                if self.str =='Ja':
                    try:
                        upphaed= int(input('Sláðu inn úttektarupphæð í heiltölum:'))
                        if upphaed < 0:
                            print('Ekki hægt að taka út neikvæða upphæð')
                            break
                        try:
                            reikn_svar= self.reikningur.taka_ut(upphaed)
                            if reikn_svar==True: print('Úttektar upphæð er {0}: '.format(upphaed))
                            elif reikn_svar==False: print('Ekki næg innistæða á reikning')
                            else: print('Villa kom upp innieign á reikning {0}:'.format(self.reikningur.inneign))
                        except:
                            print('Villa 1 kom upp')
                            break
                        self.str= input('Ný útttekt, N=Hættir?')
                        if self.str == 'N': 
                            return
                    except:
                        print('Villa  2 kom upp')
                        break
                elif self.str =='Nei': return
        self.takaUt_reikning()
    
    def saekjaStodu_reikning(self):
        return('\n Innistæða á reikning er Kr: {0}-'.format(self.reikningur.saekja_stodu()))
# =============================================================================
# Athugið. Pickle skráinn 'banki.pkl' þarf að vera til áður en keyrsla hefst       
# =============================================================================
def main():    
    reikningur= Bankareikningur()
    vskipti= Bankavidskipti(reikningur)
    reikningur.inneign= pickle.load(open('banki.pkl', 'rb'))
    while(True):
        svar= input('Sláðu inn aðgerð: \n Innsetning= \t i\n Taka út= \t\t u\n Prenta stöðu= \t p\n\t')
        if svar == 'i': vskipti.Inn_reikning()
        elif svar == 'u':vskipti.takaUt_reikning()
        elif svar == 'p': print(vskipti.saekjaStodu_reikning())
        else:break
    pickle.dump(reikningur.inneign,open('banki.pkl', 'wb'))

if __name__ == '__main__':
    main()