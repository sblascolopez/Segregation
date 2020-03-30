# Ségrégation spatiale et main invisible (Grauwin & Jensen)

import numpy as np
from random import randint

class Paramètres :
    """ Classe regroupant tous les paramètres d'une simulation """
    
    def __init__ (self,q,h,m,alpha = 0) :
        self.q = q  # définit le nombre de quartier Q = q² > ici la variable q représente le q minuscule de la relation écrite, c'est ça ?
        self.h = h  # définit le nombre d'emplacements par quartiers H = h² > même question pour h
        self.l = h*q  # taille de la ville 
        
        self.N = ((h*q)**2)/2  # Nombre d'agents initialement 
        self.alpha = alpha  # Coefficient intégrant l'altruisme
        
        self.u = lambda x : 2*x if x <= 1/2 else (2*(m-1)*x+2-m) # Fonction d'utilité des agents


class Ville :
    """Classe regroupant toutes les caractéristiques de la ville d'une simulation :
        - la ville, sous la forme d'une grille de taille l * l, contenant des 0 si l'emplacement est occupé, des 1 s'il est occupé
        - les densités de chaque quartier, sous la forme d'une grille q*q
    """
    
    def __init__ (self,ville,densites) : 
        self.ville = ville
        self.densites = densites

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
 
