# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:01:34 2025

@author: lars
"""
import math

def regne_omkrets_areal(a,b):
    areal_trekant = a*b/2
    radius = a /2
    hypotenus = (a**2 + b**2)**0.5
    halvsirkel_areal = (math.pi * radius ** 2) / 2
    halvsirkel_omkrets = (math.pi * radius + 2) * radius
    areal = round (areal_trekant + halvsirkel_areal, 2)
    omkrets = round(b + hypotenus + halvsirkel_omkrets, 2)
    return(areal, omkrets)

clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5
print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 

a = float(input("Tast inn a: "))
b = float(input("Tast inn b: "))

regn_ut = regne_omkrets_areal(a,b)

print ("Arealet av figuren er ", regn_ut[0], " og omkretsen av figuren er ", regn_ut[1])
