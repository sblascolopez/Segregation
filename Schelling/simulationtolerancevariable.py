#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:15:15 2020

@author: victorhuynh
"""

from schelling import ville, frequence, habitatconforme, swap
from simulationdebase import trace_ville
from classes import Paramètre2

def nouvelle_iteration(ville,P):
    n=np.shape(ville)[0]
    p=np.shape(ville)[1]
    i , j = randint(0,n-1) , randint(0,p-1)
    #(i,j) caractérise la position d'un ménage choisi au hasard dans l'intérieur de la ville.
    k , l = randint(0,n-1) , randint(0,p-1)

    #Mêmes variables que tout à l'heure, qui servent à alléger notre programme en complexité...
    nombre_operations1 = 0
    nombre_operations2 = 0

    #Recherche d'un ménage (i.e. emplacement habité)
    while ville[i,j] == 0 and nombre_operations1 < 50 :
        i , j = randint(0,n-1) , randint(0,p-1)
        nombre_operations1 = nombre_operations1 + 1

    #On initie une boucle while, qui identifie la classe du ménage (i,j) choisi. Ensuite, il 
    #effectue les mêmes opérations que la fonction 'itération' originelle, en prenant cette fois
    #en compte le seuil de tolérance associé la classe du ménage (i,j). 
    if ville[i,j] == 1:
        if frequence(ville,i,j) > P.Tb : 
            while (ville[k,l] != 0 or habitatconforme(ville,k,l,ville[i,j]) > P.Tb) and nombre_operations1 < 50 :
                k , l = randint(0,n-1) , randint(0,p-1)
                nombre_operations1 = nombre_operations1 + 1
            if habitatconforme(ville,k,l,ville[i,j]) <= P.Tb :
                swap(ville,i,j,k,l)
    elif ville[i,j] == 2:
        if frequence(ville,i,j)> P.Tn : 
            while (ville[k,l] != 0 or habitatconforme(ville,k,l,ville[i,j]) > P.Tn) and nombre_operations2 < 50 :
                k , l = randint(0,n-1) , randint(0,p-1)
                nombre_operations2 = nombre_operations2 + 1
            if habitatconforme(ville,k,l,ville[i,j]) <= P.Tn :
                swap(ville,i,j,k,l)
                
def nouvelle_simulation (ville,P,i_max,nb_graph) :  
    trace_ville(ville,0)
    sub_i = i_max // (nb_graph-1)   
    for i in range(1,nb_graph) :
        for j in range(sub_i) :
            nouvelle_iteration(ville,P) #Seul changement ici
        trace_ville(ville,i)

P4 = Paramètre2(50,80,7/8,1/2)
ville4=ville(P4)
nouvelle_simulation(ville4,P4,10000,8)
