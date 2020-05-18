#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:59:08 2020

@author: victorhuynh
"""

# Pour l'implémentation des modèles :
import numpy as np 
from random import randint
from numpy.random import multinomial

from classes import Paramètre

# Pour les représentations et les graphiques, on utilise principalement : 
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap

def ville (P): 
    ville = np.random.randint(0,3,(P.n,P.p)) 
    return(ville)
    
def frequence (ville, i, j) :
#ville désigne la matrice représentative de la ville.
#i désigne l'indice de la ligne du ménage qu'on étudie, entre 0 et n-1.
#j désigne l'indice de la colonne du ménage qu'on étudie, entre 0 et p-1.

    ''' 
    On utilise les notations : 
        effectif : nombre de ménages voisins de même classe que (i,j)
        total : nombre de ménages voisins quelconques de (i,j)
        f : fraction de voisins différents de (i,j)
    '''

    n,p = np.shape(ville)
    
    voisinage = ville [max(0,i-1) : min(n,i+2) , max(0,j-1) : min(p,j+2)]
    #On extrait de notre ville le voisinage du ménage (i,j) dans la variable "voisinage", 
    #c'est-à-dire la sous-matrice de "ville" qui contient ville[i,j] ainsi que les (au plus 8) 
    #coefficients adjacents. L'utilisation des fonctions min et max nous permettent de ne pas
    #obtenir de message d'erreur lorsque l'on prend des valeurs extrêmes de i et j (i.e. un ménage
    #situé à la frontière de la ville).
    
    effectif = np.sum(voisinage==ville[i,j]) - 1 
    #effectif compte le nombre de coefficients égaux à ville[i,j] dans ce voisinage, afin de 
    #compter le nombre de voisins de (i,j) qui sont de même classe que lui. 
    #On retire 1 car l'individu (i,j) fait partie de ce voisinage, il ne faut pas le compter !

    total = np.sum(voisinage!=0) - 1 
    #total compte le nombre de coefficients différents de 0 (qui signifie espace vide) dans ce 
    #voisinage, afin de compter le nombre de voisins quelconques de (i,j).
    #Pour la même raison qu'avant, on retire 1
    
    if total != 0 :
        f = 1 - (effectif/total)
    #Si le ménage possède effectivement des voisins, on calcule la fraction de voisins de même
    #classe et on en déduit celle de voisins de classe différente. 
    else :
        f = 0
    #Si le ménage n'a aucun voisin, il n'a aucun voisin de classe différente en particulier,
    #donc on a bien f=0.
    
    return f

def habitatconforme (ville, k, l, c) :
#ville désigne la matrice représentative de la ville.
#k désigne l'indice de la ligne de l'espace inhabité qu'on étudie, entre 0 et n-1.
#l désigne l'indice de la ligne de l'espace inhabité qu'on étudie, entre 0 et p-1.
#c désigne le numéro de classe du ménage qui envisage de déménager, donc c!=0.

    '''
    On réadapte les notations précédemment introduites: 
        effectif : nombre de voisins de classe c de l'emplacement (k,l).
        total : nombre d'espaces habités autour de l'emplacement (k,l).
        f : fraction de voisins qui ne sont pas de classe c de l'emplacement (k,l).
    '''

    n,p = np.shape(ville)
    
    voisinage = ville [max(0,k-1) : min(n,k+2) , max(0,l-1) : min(p,l+2)]
    #On extrait de notre ville le voisinage de l'emplacement (k,l) dans la variable "voisinage",
    #avec la même méthode que précédemment.

    effectif = np.sum(voisinage==c)  
    #Cette fois, pas besoin d'enlever 1 car l'emplacement (k,l) considéré est vide et ne sera pas 
    #compté puisque l'on choisit c != 0 !
    total = np.sum(voisinage!=0)  #Pour la même raison, pas besoin d'enlever 1
    
    if total != 0 :
        f = 1 - (effectif/total)
    else :
        f = 0
    
    return f

def swap(u,a,b,c,d): 
    u[a,b],u[c,d] = u[c,d],u[a,b]
    return(u)
    
def iteration(ville,P):
    n,p = np.shape(ville)[0], np.shape(ville)[1]
    i , j = randint(0,n-1) , randint(0,p-1)
    #i et j seront les indices de position du ménage qu'on étudiera. 
    k , l = randint(0,n-1) , randint(0,p-1)
    #k et l seront les indices de position des logements que le ménage envisagera s'il est mécontent.

    '''
    On va introduire deux variables qui vont alléger la complexité de notre programme: elles
    correspondent à des seuils maximums d'opérations qu'on s'autorise dans notre programme. La 
    seconde permet même le bon fonctionnement de notre fonction (je vous explique ça en dessous).
    '''
    nombre_operations1 = 0
    #Variable qui comptera le nombre de recherches de ménages dans la ville.
    nombre_operations2 = 0
    #Variable qui comptera le nombre de logements que le ménage aura envisagé, s'il est insatisfait.

    while ville[i,j] == 0 and nombre_operations1 < 50 :
      i , j = randint(0,n-1) , randint(0,p-1)
      nombre_operations1 = nombre_operations1 + 1
    #On choisit aléatoirement un espace (i,j) dans notre ville, jusqu'à ce qu'on tombe sur un 
    #emplacement habité par un ménage, d'où la boucle "while". Si jamais on prend 

    if frequence(ville,i,j)> (P.T) : 
    #Cas où le ménage est mécontent de son voisinage.

        while (ville[k,l] != 0 or habitatconforme(ville,k,l,ville[i,j]) >= (P.T)) and nombre_operations2 < 50 :
            k , l = randint(0,n-1) , randint(0,p-1)
            nombre_operations2 = nombre_operations2 + 1
        #Cette boucle "while" permet de trouver un espace vide qui plaira au ménage mécontent.
        #La première condition permet de trouver un espace vide.
        #La seconde condition permet à cet espace vide d'être satisfaisant.
        #La troisième permet de stopper la boucle si on ne trouve pas de lieu vide adapté:
        #au bout d'un certain moment, le ménage en aura marre de chercher un nouveau logement.

        if habitatconforme(ville,k,l,ville[i,j]) < (P.T):
            swap(ville,i,j,k,l)
        #On constitue cette boucle "if" pour déclencher le déménagement si et seulement si la 
        #boucle "while" a effectivement trouvé un logement satisfaisant pour le ménage.

    return(ville)

def schelling (P,n_iter) :  
    ma_ville = ville (P)
    for i in range(n_iter) :
        iteration(ma_ville,P)

        
