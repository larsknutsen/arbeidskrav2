# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 12:38:42 2025

@author: lars
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.61],
        "Italia": ["Roma", 2.873],
        }

clear2 = "\n" * 2 #legger 2 linjeskift til variabel clear2
clear5 = "\n" * 5 #legger 5 linjeskift til variabel clear5

print (clear5) #printer variabel clear5 (linjeskiftene) for å gjøre konsollet mer lesbart 

print(data) #for å kunne se data før inntasting av nye data

print (clear2) #printer variabel clear2 (linjeskiftene5) for å gjøre konsollet mer lesbart


nytt_land = input("Tast inn nytt land: ")
ny_hovedstad = input("Tast inn hovedstaden: ")
ny_innbyggere = input("Tast inn antall inbyggere: ")

data[nytt_land] = [ny_hovedstad, ny_innbyggere]

print (clear2) #for lesbarhet
print ("Dette er alle data etter siste oppdatering: ")
print(data) #for å se at det nye landet med hovedstad og hovedstadens innbygger er kommet med

