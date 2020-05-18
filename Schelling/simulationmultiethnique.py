#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:18:39 2020

@author: victorhuynh
"""
import numpy as np

import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

from schelling import frequence, habitatconforme, swap
from classes import Paramètre

def ville_multiethnique (P): 
    ville = np.random.randint(0,5,(P.n,P.p))
    #La ville peut désormais contenir des 3 et des 4 en plus des 0, 1 et 2.
    return(ville)

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

P5 = Paramètre(50,80,1/2) 
#On reprend le premier format de paramètres car on a un cas avec un unique seuil de tolérance.
ville5 = ville_multiethnique(P5)
simulation_multiethnique(ville5,P5,100000,8)