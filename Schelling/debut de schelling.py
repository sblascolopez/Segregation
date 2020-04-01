#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:17:27 2020

@author: victorhuynh
"""

import numpy as np
import string as str

#version facile où on a un individu par emplacement, et tous les emplacements sont remplis

def ville (n,p): 
    ville = np.random.randint(0,3,(n,p)) #crée une ville de taille n x p avec des 0 si on a un blanc, 1 si on a un black, 2 si on a un espace vide
    return(ville)
    
def swap(u,a,b,c,d):
    u[a,b],u[c,d] = u[c,d],u[a,b]
    return(u)

def satisfaction (n,p,i,j,T): #on crée une ville de taille (n+2) x (p+2) pour représenter la ville et le début de la ville d'à côté, on prend l'individu à l'emplacement (i,j), et on se fixe un seuil de tolérance T
    u=ville(n+2,p+2)
    effectif = 0
    total=0
    print(u)
    if u[i-2,j-1] == u[i-1,j-1] : #on teste pour chaque voisin s'il est différent ou non
        effectif = effectif + 1
        total = total + 1
    elif u[i-2,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i,j-1] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-2,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-2,j+2] == u[i-1,j-1] :
        effectif = effectif + 1
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+2,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+2,j+2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
            total = total + 1
    f=1-(effectif/total)
    if f>T: #on compare la fréquence de voisins différents au seuil de tolérance
        print ("il déménage")  #je vais ensuite programmer son déménagement
        destination_possible = np.argwhere(u==2) #on cherche tous les lieux vides dans la ville et sa frontière
        destination_choisie = [destination_possible[0][0],destination_possible[0][1]] #on prend le premier emplacmeent vide
        swap(u,i-1,j-1,destination_possible[0][0],destination_possible[0][1])
        print(u)
    else:
        print ("il reste")
        

#si à l'indice (i,j) on avait un emplacement vide, ça ne fait rien car il va échanger de place avec un autre emplacement vide