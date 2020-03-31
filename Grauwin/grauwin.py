# Ségrégation spatiale et main invisible (Grauwin & Jensen)


import numpy as np
from random import randint

from numpy.random import binomial
from math import exp


from classes import Ville, Paramètres


# Définissions une première fonction qui initialise la simulation en créant une ville 
        
def init_ville (p) :
    
    ville = np.zeros((p.l,p.l),dtype=int) #crée une matrice remplie de zéros de la taille de la ville > tous les emplacements sont vides à ce stade
    n = p.N #on initialise n avec le nombre d'habitants
    while n > 0 : #étape qui sert à peupler la ville avec nos n habitants
        i , j = randint(0,p.l-1) , randint(0,p.l-1) #on prend des emplacements aux hasards, de ligne i et colonne j
        if ville[i,j] == 0 : #si l'emplacement n'est pas pris, alors on place un individu dedans
            ville[i,j] = 1
            n=n-1
    
    densites = np.zeros((p.q,p.q)) #crée une matrice de zéros de taille qxq, qui représente les q² quartiers
    H = (p.h)**2 #nombre d'emplacements par quartiers
    for i in range(p.q) :
        for j in range(p.q) : #la double boucle for permet de survoler chaque quartier
            d = np.sum(ville[i*p.h : (i+1)*p.h-1 , j*p.h : (j+1)*p.h-1]) #on prend la ville créée précédemment, on compte le nombre d'habitants du quartier
            densites[i,j] = d/H #calcul de la densité du quartier de ligne i et de colonne j 
    
    return Ville(ville,densites)
 
        
        
# On définit ensuite une fonction qui actualise une ville en proposant à un individu au hasard de déménager. Cette fonction modifie directement la ville et ne renvoie rien.
    

def actualise (ville,p) :
    h=p.h
    # On commence par choisir un individu et une emplacement vacant au hasard (dans un quartier différent)
    indiv = (-1,-1)
    emplacement = (-1,-1)
    while indiv == (-1,-1) :
        i , j = randint(0,p.l-1) , randint(0,p.l-1)
        if ville.ville[i,j]!=0 :
            indiv = (i,j)
    while emplacement == (-1,-1) :
        i , j = randint(0,p.l-1) , randint(0,p.l-1)
        if all([ville.ville[i,j]==0, (indiv[0]//h)-1 != (i//h)-1, (indiv[1]//h)-1 != (j//h)-1]) :
            emplacement = (i,j)
    print(indiv,emplacement)        
    # Ensuite, on propose à cet individu de déménager selon une loi de logit
    H = (p.h)**2
    u=p.u
    u1 = u(ville.densites[(indiv[0]//h-1), (indiv[1]//h-1)])
    u2 = u(ville.densites[(emplacement[0]//h-1), (emplacement[1]//h-1)]) + 1/H
    p = 1 / (1 + exp(- (u2-u1) / p.T))
    if binomial(1,p) :
        ville.ville[indiv[0],indiv[1]] = 0
        ville.ville[emplacement[0],emplacement[1]] = 1
        ville.densites[indiv[0]//h-1,indiv[1]//h-1] -= 1/H
        ville.densites[emplacement[0]//h-1,emplacement[1]//h-1] += 1/H

        
