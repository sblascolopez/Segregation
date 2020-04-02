#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:17:27 2020

@author: victorhuynh
"""

import numpy as np
import string as str

#Modèle: on a un individu par emplacement, et tous les emplacements sont remplis


#Idée de programme 1 : on crée une ville de taille nxp avec sa frontière extérieure, on prend un citoyen au hasard dedans, s'il est satisfait de son voisinage il reste, sinon il se déplace vers le premier emplacement vide qu'il trouve. 

#Premier jet: son défaut, c'est qu'à chaque utilisation de la fonction satisfaction, il recrée une nouvelle ville

def ville (n,p): 
    ville = np.random.randint(0,3,(n,p)) #crée une ville de taille n x p avec des 0 si on a un blanc, 1 si on a un black, 2 si on a un espace vide
    return(ville)
    
def swap(u,a,b,c,d):
    u[a,b],u[c,d] = u[c,d],u[a,b]
    return(u)

def satisfaction1 (n,p,i,j,T): #on crée une ville de taille (n+2) x (p+2) pour représenter la ville et le début de la ville d'à côté, on prend l'individu à l'emplacement (i,j), et on se fixe un seuil de tolérance T
    u=ville(n+2,p+2)
    effectif = 0
    total=0
    print(u)
    if u[i-2,j-1] == u[i-1,j-1] : #on teste pour chaque voisin s'il est différent ou non
        effectif = effectif + 1
        total = total + 1
    elif u[i-2,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i,j-1] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-2,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-2,j+2] == u[i-1,j-1] :
        effectif = effectif + 1
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+2,j-2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+2,j+2] == u[i-1,j-1] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
            total = total + 1
    f=1-(effectif/total)
    if f>T: #on compare la fréquence de voisins différents au seuil de tolérance
        print ("il déménage")  #je vais ensuite programmer son déménagement
        destination_possible = np.argwhere(u==2) #on cherche tous les lieux vides dans la ville et sa frontière
        destination_choisie = [destination_possible[0][0],destination_possible[0][1]] #on prend le premier emplacmeent vide
        swap(u,i-1,j-1,destination_possible[0][0],destination_possible[0][1])
        print(u)
    else:
        print ("il reste")
        

#Si à l'indice (i,j) on avait un emplacement vide, ça ne fait rien car il va échanger de place avec un autre emplacement vide: c'est comme si on avait pas appliqué la fonction en fait.
        
        
        
        
        
        
        
        
#Deuxième jet: on crée une ville au départ, qu'on garde et qui va subir des modifications au fur et à mesure des itérations de la fonction satisfaction
        
        
def ville (n,p): 
    ville = np.random.randint(0,3,(n+2,p+2)) #crée matrice (n+2)x(p+2) qui correspond à une ville de taille nxp et sa frontière extérieure d'épaisseur 1. On a des 0 si on a un blanc, 1 si on a un black, 2 si on a un espace vide
    return(ville)
    
def swap(u,a,b,c,d):
    u[a,b],u[c,d] = u[c,d],u[a,b]
    return(u)

u = ville(8,8)  #on crée une ville de taille (n+2) x (p+2) pour représenter la ville et le début de la ville d'à côté, on prend l'individu à l'emplacement (i,j), et on se fixe un seuil de tolérance T

def satisfaction (u,i,j,T): #prendre i et j entre 1 et n, T entre 0 et 1
    effectif = 0
    total=0
    print(u) #montre la ville avant déménagement
    if u[i-1,j] == u[i,j] : #on teste pour chaque voisin s'il est différent ou non
        effectif = effectif + 1
        total = total + 1
    elif u[i-1,j] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j-1] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i-1,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i,j-1] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+1,j-1] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i+1,j-1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+1,j] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i+1,j] == 2 :
        total = total
    else :
        total = total + 1
    if u[i+1,j+1] == u[i,j] :
        effectif = effectif + 1
        total = total + 1
    elif u[i+1,j+1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i,j+1] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j+1] == 2 :
        total = total
    else :
        total = total + 1
    if u[i-1,j+1] == u[i,j] :
        effectif = effectif + 1 
        total = total + 1
    elif u[i,j+1] == 2 :
        total = total
    else :
            total = total + 1
    f=1-(effectif/total)
    if f>T: #on compare la fréquence de voisins différents au seuil de tolérance
        print ("il déménage")  #je vais ensuite programmer son déménagement
        destination_possible = np.argwhere(u==2) #on cherche tous les lieux vides dans la ville et sa frontière
        destination_choisie = [destination_possible[0][0],destination_possible[0][1]] #on prend le premier emplacmeent vide
        swap(u,i,j,destination_possible[0][0],destination_possible[0][1])
        return(u)
    else:
        print ("il reste")
        
        
#Idée de programme 2 (qui reprend essentiellement le premier) : on crée une ville de taille nxp avec sa frontière extérieure, on prend un citoyen au hasard dedans, s'il est satisfait de son voisinage il reste, sinon il se déplace vers le premier emplacement vide qu'il trouve et qui a un voisinage qui lui est satisfaisant.  

