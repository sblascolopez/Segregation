#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:04:39 2020

@author: victorhuynh
"""

import numpy as np

from classes import Paramètre
from schelling import ville, iteration

import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

def trace_ville (ville,i) :  # i est le numéro de la figure
    
    #On initialise la figure et on règle les axes :
    fig = plt.figure(i)
    ax = plt.axes(xlim=(-0.5,np.shape(ville)[1]-0.5), ylim=(-0.5,np.shape(ville)[0]-0.5)) 
    #Crée les axes des abscisses et ordonnées avec des longueurs adaptées à la taille de ma ville.
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect("equal")
    
    #On place ensuite les individus :
    cmap = ListedColormap([(1,1,1),(1,0.8,0.8),(0,0,0)]) 
    #Couleurs choisies, indiquées selon leur code RVB
    img = plt.imshow(ville, cmap=cmap) 
    plt.draw()
    
def simulation (ville,P,i_max,nb_graph) :  
#i_max désigne le nombre total d'itérations, et nb_graph le nombre de graphiques à afficher.
#Ces paramètres sont à choisir de sorte que i_max divisible par (nb_graph-1).
#T désigne le seuil de tolérence commun à tous les ménages de la ville.
    trace_ville(ville,0)
    sub_i = i_max // (nb_graph-1) 
    #sub_i correspond au nombre d'itérations qu'on effectuera entre chaque graphique.
    for i in range(1,nb_graph) :
        for j in range(sub_i) :
            iteration(ville,P)
    #Pour tout graphique i, on effectue sub_i itérations.
        trace_ville(ville,i)
    #Représente graphiquement le dernier état de la ville

#Simulation
    
P2 = Paramètre(50,80,1/2)
ville2=ville(P2)
simulation(ville2,P2,100000,8)