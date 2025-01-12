# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:45:26 2025

@author: lars
"""
import math

clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5
print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 

antall_elever = int(input('Skriv inn antall elever:' ))
antall_pizza = int(math.ceil(antall_elever/4))

print("Du trenger", antall_pizza, "pizzaer til klassefesten")
