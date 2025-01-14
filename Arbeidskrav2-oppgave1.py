# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:40:32 2025

@author: lars
"""

from datetime import datetime

clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5
print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 

dagens_ar = datetime.now().year #henter dagens årstall
alder = int(input("Hvilket år er du født? "))
gammel = dagens_ar-alder #regner ut alder i antall år

print("Du er", gammel, "år gammel")


