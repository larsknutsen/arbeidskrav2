# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 12:11:18 2025

@author: lars
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.61],
        "Italia": ["Roma", 2.873],
        }


clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5
print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 


land = input("Tast inn land: ")


print(data[land][0], " er hovedstaden i ", land , "og det er ", data[land][1], " millioner innbyggere i ", data[land][0])

