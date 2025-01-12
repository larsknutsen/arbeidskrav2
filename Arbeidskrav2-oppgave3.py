# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:58:24 2025

@author: lars
"""
import numpy as np

clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5
print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 


v_grad = float(input('Skriv inn gradtallet:' ))


def funksjon_rad(grad):
    rad = grad*np.pi/180
    return rad

v_rad = round(funksjon_rad(v_grad), 2)

print ('Radiantallet er', v_rad) 
"jeg kjenner ikke så godt til radianer og grader, men antar det er en fordel å runde av til 2 desimaler (?)"
