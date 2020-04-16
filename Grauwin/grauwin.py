# Ségrégation spatiale et main invisible (Grauwin & Jensen)


import numpy as np
from random import randint

from numpy.random import binomial
from math import exp


from classes import Ville, Paramètres, U



# Définissions une première fonction qui initialise la simulation en créant une ville avec une répartition aléatoire des individus
        
def init_ville (p) :
    ville = np.zeros((p.l,p.l),dtype=int)
    n_alpha = int(p.alpha * p.N)  #nombre d'habitants altruistes qui sont encore à placer
    n = p.N - n_alpha  #nombre d'habitants égoïstes qui sont encore à placer
    
    #On commence par placer les altruistes :
    while n_alpha > 0 :    #tant qu'il n'y a pas n_alpha habitants altruistes dans la ville, on continue 
        i , j = randint(0,p.l-1) , randint(0,p.l-1) 
        if ville[i,j] == 0 : 
            ville[i,j] = 2
            n_alpha -=1    
    #Ensuite, on place les autres habitants (égoistes) :
    while n > 0 : 
        i , j = randint(0,p.l-1) , randint(0,p.l-1)  
        if ville[i,j] == 0 :
            ville[i,j] = 1
            n-=1
            
    #On crée ensuite la matrice des densités par quartiers
    densites = np.zeros((p.q,p.q)) 
    H = (p.h)**2 #nombre d'emplacements par quartiers
    for i in range(p.q) :
        for j in range(p.q) : 
            d = np.sum(ville[i*p.h : (i+1)*p.h-1 , j*p.h : (j+1)*p.h-1]!=0) #compte le nombre d'habitants dans le quartier (i,j)
            densites[i,j] = d/H 
    
    return Ville(ville,densites)
 


# On définit ensuite une fonction qui actualise une ville en proposant à un individu au hasard de déménager. Cette fonction modifie directement la ville et ne renvoie rien.
    
def actualise (ville,p) :
    h=p.h
    # On commence par choisir un individu et une emplacement vacant au hasard (dans un quartier différent)
    indiv = (-1,-1)
    emplacement = (-1,-1)
    while indiv == (-1,-1) :
        i , j = randint(0,p.l-1) , randint(0,p.l-1)
        if ville.ville[i,j] != 0 :
            indiv = (i,j)
    while emplacement == (-1,-1) :
        i , j = randint(0,p.l-1) , randint(0,p.l-1)
        if all([ville.ville[i,j]==0, (indiv[0]//h) != (i//h), (indiv[1]//h) != (j//h)]) :  #s'assure que l'emplacement est vide et dans un quartier différent. L'avantage de la fonction all est que l'exécution s'arrête dès qu'une condition n'est pas remplie (gain de temps)
            emplacement = (i,j)
                  
    # Ensuite, on calcule les nouvelles et anciennes densités avant (0) et après (1) déménagement, dans le quartier de départ (i) et celui d'arrivée (e), pour en déduire les différences d'utilité
    H = (p.h)**2
    u=p.u
    
    rho_i0 = ville.densites[(indiv[0]//h),(indiv[1]//h)]
    rho_i1 = rho_i0 - 1/H
    rho_e0 = ville.densites[(emplacement[0]//h),(emplacement[1]//h)]
    rho_e1 = rho_e0 + 1/H
    
    if ville.ville[indiv[0],indiv[1]] == 1 :  #individu égoïste 
        delta_u = u(rho_e1) - u(rho_i0)  #différence d'utilité liée au déménagement
    else :  #individu altruiste
        delta_u = rho_i1*u(rho_i1) + rho_e1*u(rho_e1) - rho_i0*u(rho_i0) - rho_e0*u(rho_e0) #différence d'utilité liée au déménagement
    
    #On propose ensuite à l'individu de déménager selon la probabilité p calculée à partir de la loi de logit
    p = 1 / (1 + exp( - (delta_u) / p.T))
    if binomial(1,p) :  #renvoie 1 (déménagement) avec la probabilité p, et 0 (non déménagement) sinon
        ville.ville[indiv[0],indiv[1]], ville.ville[emplacement[0],emplacement[1]] = ville.ville[emplacement[0],emplacement[1]], ville.ville[indiv[0],indiv[1]]
        ville.densites[(indiv[0]//h),(indiv[1]//h)] -= 1/H
        ville.densites[(emplacement[0]//h),(emplacement[1]//h)] += 1/H

   
     
# Ainsi, le programme permettant de réaliser une simulation peut s'écrire simplement de la manière suivante :

def grauwin (p, n_iter) :  #n_iter est le nombre d'itérations
    ville = init_ville (p)
    for i in range(n_iter) :
        actualise(ville,p)
    return ville
    