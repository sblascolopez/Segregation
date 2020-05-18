#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:22:44 2020

@author: victorhuynh
"""

import numpy as np
from numpy.random import multinomial

import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

from simulationdebase import iteration
from classes import Paramètre3, Paramètre4

def ville_realiste1 (P): 
    #n et p caractérisent toujours la taille de notre ville. 
    #Les proportions d'espaces vides et d'individus de chaque classe sont à choisir de sorte que 
    #leur somme vaille 1.

    ma_ville = np.zeros((P.n,P.p))
    #Je crée une matrice de taille n*p : pour le moment, son contenu n'a pas d'importance.

    #On initie une double-boucle "for" pour prendre un par un chaque coefficient de la matrice. 
    for i in range(0,P.n):
        for j in range(0,P.p):  
            ma_ville[i,j] = np.argwhere(multinomial(1,[P.proportion_vides,P.proportion_blancs,P.proportion_noirs])==1)
    #On simule une loi multinomiale de paramètre n=1 qui prendra une valeur entre 0 et 4, selon les
    #proportions rentrées. La fonction multinomial affiche un vecteur de taille 5, où le (i+1)-ème
    #coefficient affiche le nombre de fois la valeur i a été prise. Comme n=1, seule une des 5 
    #valeurs sera prise: ce vecteur contiendra donc quatre coefficients "0", et un seul "1" dont
    #l'indice de position indique la valeur qui a été prise. On utilise alors np.argwhere pour 
    #déduire cette dernière, et attribuer au ménage (i,j) sa classe. 

    return(ma_ville)

'''
La fonction `ville_realiste2` reprend essentiellement la première, en prenant désormais en compte  
2 nouvelles classes supplémentaire: on a donc deux nouveaux paramètres d'entrée, qui correspondent 
aux proportions de ménages appartenant à ces eux classes dans la ville. 
'''

def ville_realiste2 (P): 
    #Les proportions sont toujours à choisir de sorte que leur somme vaille 1.
    ma_ville = np.zeros((P.n,P.p))

    for i in range(0,P.n):
        for j in range(0,P.p):
            ma_ville[i,j] = np.argwhere(multinomial(1,[P.proportion_vides,P.proportion_blancs,P.proportion_noirs,P.proportion_asiats,P.proportion_latinos])==1)
  
    return(ma_ville)
    
def trace_ville_multiethnique (ville,i) :  # i est le numéro de la figure
    fig = plt.figure(i)
    ax = plt.axes(xlim=(-0.5,np.shape(ville)[1]-0.5), ylim=(-0.5,np.shape(ville)[0]-0.5)) 
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect("equal")
    
    cmap = ListedColormap([(1,1,1),(1,0.8,0.8),(0,0,0),(0.8,1,0.8),(0.8,0.8,1)]) 
    #On ajoute deux nouvelles couleurs pour les deux nouvelles classes
    img = plt.imshow(ville, cmap=cmap) 
    plt.draw()

def simulation_multiethnique (ville,P,i_max,nb_graph) :  
#A choisir de sorte que i_max divisible par (nb_graph-1)
    trace_ville_multiethnique(ville,0)
    sub_i = i_max // (nb_graph-1)   
    # Nombre d'itérations entre chaque graphique
    for i in range(1,nb_graph) :
        for j in range(sub_i) :
            iteration(ville,P)
        trace_ville_multiethnique(ville,i) #On prend en compte la nouvelle fonction de tracé.

#Simulation:

P6 = Paramètre4(50,80,1/2,0.1,0.3,0.25,0.25,0.1)
ville6=ville_realiste2(P6)
simulation_multiethnique(ville6,P6,100000,8)
