#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:17:04 2019

@author: nestIH
"""
import laxinn
import random

class Veidimadur:
    def __init__(self, nafn):
        self.nafn= nafn
        self.fjoldi_veidra=0
        self.fjoldi_slepta= 0
        
    def veida(self):
        nafn= str
        lax=laxinn.Lax()
        lax.fjoldi_fiska= 3
        while(True):
            fiskur= random.randint(0,1)
            lax.aldur= random.randint(3,5)

            if fiskur == 1: 
                nafn ='hrigna'
                lax.hrigna_ = lax.hrigna_ + 1 
            else:
                nafn = 'haengur'
                lax.haengur_ = lax.haengur_  + 1
            lax.fjoldi_fiska= lax.fjoldi_fiska - 1
            lax.nafn= nafn
            lax.synda()
            self.sleppa(lax)
            if lax.fjoldi_fiska == 0: 
                break

            
    def sleppa(self, lax):
        if lax.nafn == 'hrigna':
            lax.fjoldi_fiska= lax.fjoldi_fiska + 1
            self.fjoldi_slepta= self.fjoldi_slepta +1
        self.fjoldi_veidra= self.fjoldi_veidra + 1
        print('fjöldi eftir að veiða =:',lax.fjoldi_fiska)

    #Grafísk framsettning á niðurstöðum. Hannið sjálf þetta fall
    def laxa_graf(self):
        pass
    
def main():
    laxveidi= Veidimadur('kalli')
    laxveidi.veida()
    print('\nVeiðimaðurinn {0} hefur veitt alls {1} laxa og slept {2} hrignum'
          .format(laxveidi.nafn, laxveidi.fjoldi_veidra, laxveidi.fjoldi_slepta))
    

if __name__ == '__main__':
    main()