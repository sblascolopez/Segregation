#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:51:32 2020

@author: victorhuynh
"""

def ville (n,p): 
    ville = np.random.randint(0,3,(n+2,p+2)) 
    #La matrice est de taille (n+2)*(p+2) car elle représente
    #à la fois la ville et sa frontière extérieure.
    for j in range(0,p+2):
        if ville[0,j]==0:
            ville[0,j] = np.random.randint(1,3)
        if ville[n+1,j]==0:
            ville[n+1,j] = np.random.randint(1,3)
    for i in range(0,n+2):
        if ville[i,0]==0:
            ville[i,0] = np.random.randint(1,3)
        if ville[i,p+1]==0:
            ville[i,p+1] = np.random.randint(1,3)
    #Ces deux boucles "for" permettent de faire habiter tous les espaces en frontière.
    return(ville)
    
    

#Dans cette version, on prenait i entre 1 et n et j entre 1.
#ville[i,j] nous donnait alors toujours la classe d'un ménage
#situé strictement à l'intérieur de la ville.


def frequence (ville,i,j): 
#Où i et j caractérisent la position d'un ménage à l'intérieur de la ville
#Dans cette version on choisit i entre 1 et n et j entre 1 et p. En langage Python, les indices sont 
#décalés. Donc le ménage (i,j) est représenté par le coefficient ville[i-1,j-1].
    effectif = 0
    total=0
    if ville[i-1,j] == ville[i,j] : 
        effectif = effectif + 1
        total = total + 1
    elif ville[i-1,j] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i-1,j-1] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i-1,j-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i,j-1] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i,j-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i+1,j-1] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i+1,j-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i+1,j] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i+1,j] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i+1,j+1] == ville[i,j] :
        effectif = effectif + 1
        total = total + 1
    elif ville[i+1,j+1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i,j+1] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i,j+1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[i-1,j+1] == ville[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif ville[i-1,j+1] == 0 :
        total = total
    else :
            total = total + 1
    if total == 0:
        f=0
    else:
        f=1-(effectif/total)
    return(f)
    

def habitatconforme (ville,k,l,c):
#c représente la classe de l'individu qui envisage de déménager sur l'emplacement (k,l).
    effectif = 0
    total=0
    if ville[k-1,l] == c :
        effectif = effectif + 1
        total = total + 1
    elif ville[k-1,l] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k-1,l-1] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k-1,l-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k,l-1] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k,l-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k+1,l-1] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k+1,l-1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k+1,l] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k+1,l] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k+1,l+1] == c :
        effectif = effectif + 1
        total = total + 1
    elif ville[k+1,l+1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k,l+1] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k,l+1] == 0 :
        total = total
    else :
        total = total + 1
    if ville[k-1,l+1] == c :
        effectif = effectif + 1 
        total = total + 1
    elif ville[k-1,l+1] == 0 :
        total = total
    else :
            total = total + 1
    if total == 0:
        f=0
    else:
        f=1-(effectif/total)
    return(f)
    
