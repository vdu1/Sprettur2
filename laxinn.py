#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:12:15 2019

@author: nestIH
"""

class Lax:
    def __init__(self, nafn='lax', aldur=0, fjoldi_fiska=0):
        self.nafn= nafn
        self.aldur = aldur
        self.fjoldi_fiska= fjoldi_fiska
        self.hrigna_=  0
        self.haengur_= 0
        
    def synda(self):
        print(self.nafn + ' er ad synda')
        self.vera_godur()
        
    def vera_godur(self):
        print(self.nafn + ' er godur')
        self.vera_aldur()
        
    def vera_aldur(self):
         print(self.nafn + ' er {0} ára'.format(self.aldur))

def main():
    print('Þetta er skraínn Lax')
    
if __name__ == '__main__':
    print('Keyri eigin skrá´')
    main()
else:
    print('Skráin er importuð í aðra skrá')
