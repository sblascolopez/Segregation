#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:17:27 2020

@author: victorhuynh
"""

import numpy as np

#version facile où on a un individu par emplacement, et tous les emplacements sont remplis

def ville (n,p): 
    ville = np.random.randint(0,2,(n,p)) #crée une ville de taille n x p avec des 0 si on a un blanc, 1 si on a un black 
    return(ville)

def satisfaction (n,p,i,j,T): #on crée une ville de taille n x p, on prend l'individu à l'emplacement (i,j), et on se fixe un seuil de tolérance T
    u=ville(n,p)
    effectif = 0
    if (i>=2 and j>=2 and i <= (n-1) and j <= (p-1)): #cas où l'on prend un citoyen dans l'intérieur de la ville
        if u[i-2,j-1] != u[i-1,j-1] : #on teste pour chaque voisin s'il est différent ou non
            effectif = effectif + 1
        if u[i,j-1] != u[i-1,j-1] :
            effectif = effectif + 1 
        if u[i-1,j-2] != u[i-1,j-1] :
            effectif = effectif + 1 
        if u[i-1,j] != u[i-1,j-1] :
            effectif = effectif + 1 
        f=effectif/4 
    else: #cas où le citoyen se situe à la frontière
        print ("ça je sais pas encore comment le faire")
    if f>T: #on compare la fréquence de voisins différents au seuil de tolérance
        print ("il déménage")
    else:
        print ("il reste")
    