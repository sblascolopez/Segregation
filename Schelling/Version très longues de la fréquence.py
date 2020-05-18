#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:47:29 2020

@author: victorhuynh
"""

def frequence (ville,i,j): 
#Où i et j caractérisent la position d'un ménage à l'intérieur de la ville
#Dans cette version on choisit i entre 1 et n et j entre 1 et p. En langage Python, les indices sont 
#décalés. Donc le ménage (i,j) est représenté par le coefficient ville[i-1,j-1].

    effectif = 0 #Représentera le nombre de ménages voisins de même classe que (i,j).
    total = 0 #Représentera le nombre de ménages voisins quelconques de (i,j).
    f = 0 #Représentera la fraction de voisins différents de (i,j).
    
    if (i,j) == (1,1) : #Si le ménage vit sur le coin Nord-Ouest : il n'a que 3 espaces voisins.
        if ville[i-1,j] == ville[i-1,j-1] :
            effectif = effectif + 1
            total = total + 1
        #Cette première boucle "if" vérifie d'abord si le premier espace voisin est habité par un
        #ménage de même classe que (i,j) (i.e. ville[i-1,j] == ville[i-1,j-1]). Si c'est le cas, le
        #compteur de ménages voisins semblables et celui de ménages voisins quelconques augmentent. 
        elif ville[i-1,j] != 0 :
            total = total + 1
        #Si cet espace voisin est habité (i.e. ville[i-1,j] != 0) par un ménage d'une autre classe,
        #alors seul le compteur de ménages voisins quelconques augmente. Fin de la boucle "if". 
        #On la répète pour tous les autres trespaces voisins du ménage (i,j).
        if ville[i,j] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1
    
    elif (i,j) == (1,np.shape(ville)[1]) : 
    #Si le ménage vit sur le coin Nord-Est : il n'a que 3 espaces voisins.
        if ville[i-1,j-2] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i,j-2] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j-2] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1

    elif (i,j) == (np.shape(ville)[0],1) : 
    #Si le ménage vit sur le coin Sud-Ouest : il n'a que 3 espaces voisins.
        if ville[i-1,j] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-1,j] != 0 :
            total = total + 1
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
        if ville[i-2,j] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j] != 0 :
            total = total + 1
            
    elif (i,j) == (np.shape(ville)[0],np.shape(ville)[1]) : 
    #Si le ménage vit sur le coin Nord-Est : il n'a que 3 espaces voisins.
        if ville[i-1,j-2] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i-2,j-2] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-2] != 0 :
            total = total + 1
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
            
    elif i == 1 and j in range(2,np.shape(ville)[1]):
    #Si le ménage vit sur la frontière Nord de la ville: il n'a que 5 espaces voisins.
        if ville[i-1,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-2] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1
        if ville[i,j] == ville[i-1,j-1] :
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j] != 0 :
            total = total + 1
        if ville[i-1,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j] != 0 :
            total = total + 1
            
    elif i == np.shape(ville)[0] and j in range(2,np.shape(ville)[1]):
    #Si le ménage sur la frontière Sud de la ville: il n'a que 5 espaces voisins.
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
        if ville[i-2,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j-2] != 0 :
            total = total + 1
        if ville[i-1,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i-1,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j] != 0 :
            total = total + 1
        if ville[i-2,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j] != 0 :
            total = total + 1
    
    elif i in range(2,np.shape(ville)[0]) and j == 1 :    
    #Si le ménage vit sur la frontière Ouest de la ville: il n'a que 5 espaces voisins.
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1
        if ville[i,j] == ville[i-1,j-1] :
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j] != 0 :
            total = total + 1
        if ville[i-1,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j] != 0 :
            total = total + 1
        if ville[i-2,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j] != 0 :
            total = total + 1
        
    elif i in range(2,np.shape(ville)[0]) and j == np.shape(ville)[1] :
    #Si le ménage sur la frontière Est de la ville: il n'a que 5 espaces voisins.
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
        if ville[i-2,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j-2] != 0 :
            total = total + 1
        if ville[i-1,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-2] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1
    
    else : 
    #Si le ménage vit dans l'intérieur de la ville: il a 8 espaces voisins.
        if ville[i-2,j-1] == ville[i-1,j-1] : 
            effectif = effectif + 1
            total = total + 1
        elif ville[i-2,j-1] != 0 :
            total = total + 1
        if ville[i-2,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j-2] != 0 :
            total = total + 1
        if ville[i-1,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j-2] != 0 :
            total = total + 1
        if ville[i,j-2] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-2] != 0 :
            total = total + 1
        if ville[i,j-1] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i,j-1] != 0 :
            total = total + 1
        if ville[i,j] == ville[i-1,j-1] :
            effectif = effectif + 1
            total = total + 1
        elif ville[i,j] != 0 :
            total = total + 1
        if ville[i-1,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-1,j] != 0 :
            total = total + 1
        if ville[i-2,j] == ville[i-1,j-1] :
            effectif = effectif + 1 
            total = total + 1
        elif ville[i-2,j] != 0 :
            total = total + 1
            
    #Si le ménage possède effectivement des voisins, on calcule la fraction de voisins de même
    #classe et on en déduit celle de voisins de classe différente. 
    if total != 0:
        f=1-(effectif/total)
    #Si le ménage n'a aucun voisin, il n'a aucun voisin de classe différente en particulier,
    #donc on a bien f=0 (valeur initiale de la variable f, qu'on laisse inchangée).
    
    return(f)
    
    
def habitatconforme (ville,k,l,c):

#Où k et l représentent la position de l'espace vide dans la ville et c représente la classe de 
#l'individu qui envisage de déménager à l'emplacement (k,l).
    
    effectif = 0 #Représentera le nombre de voisins de classe c de l'emplacement (k,l).
    total = 0 #Représentera le nombre d'espaces habités autour de l'emplacement (k,l).
    f = 0 #Représentera la fraction de voisins qui ne sont pas de classe c de l'emplacement (k,l).
    
    if (k,l) == (1,1) : 
    #Si l'habitat se situe sur le coin Nord-Ouest, il n'a que 3 espaces voisins.
        if ville[k-1,l] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
        if ville[k,l] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l] != 0 :
            total = total + 1
        if ville[k,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1
    
    elif (k,l) == (1,np.shape(ville)[1]) : 
    #Si l'habitat se situe sur le coin Nord-Est, il n'a que 3 espaces voisins.
        if ville[k-1,l-2] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k,l-2] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l-2] != 0 :
            total = total + 1
        if ville[k,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1

    elif (k,l) == (np.shape(ville)[0],1) : 
    #Si l'habitat se situe sur le coin Sud-Ouest, il n'a que 3 espaces voisins.
        if ville[k-1,l] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
        if ville[k-2,l] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l] != 0 :
            total = total + 1
            
    elif (k,l) == (np.shape(ville)[0],np.shape(ville)[1]) : 
    #Si l'habitat se situe sur le coin Sud-Est, il n'a que 3 espaces voisins.
        if ville[k-1,l-2] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k-2,l-2] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-2] != 0 :
            total = total + 1
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
            
    elif k == 1 and l in range(2,np.shape(ville)[1]):
    #Habitat sur la frontière Nord de la ville: n'a que 5 espaces voisins
        if ville[k-1,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-2] != 0 :
            total = total + 1
        if ville[k,l-1] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1
        if ville[k,l] == c :
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l] != 0 :
            total = total + 1
        if ville[k-1,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
            
    elif k == np.shape(ville)[0] and l in range(2,np.shape(ville)[1]):
    #Habitat sur la frontière Sud de la ville: n'a que 5 espaces voisins
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
        if ville[k-2,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l-2] != 0 :
            total = total + 1
        if ville[k-1,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k-1,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
        if ville[k-2,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l] != 0 :
            total = total + 1
    
    elif k in range(2,np.shape(ville)[0]) and l == 1 :    
    #Habitat sur la frontière Ouest de la ville: n'a que 5 espaces voisins
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
        if ville[k,l-1] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1
        if ville[k,l] == c :
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l] != 0 :
            total = total + 1
        if ville[k-1,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
        if ville[k-2,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l] != 0 :
            total = total + 1
        
    elif k in range(2,np.shape(ville)[0]) and l == np.shape(ville)[1] :
    #Habitat sur la frontière Est de la ville: n'a que 5 espaces voisins
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
        if ville[k-2,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l-2] != 0 :
            total = total + 1
        if ville[k-1,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-2] != 0 :
            total = total + 1
        if ville[k,l-1] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1
    
    else : 
    #Habitat dans l'intérieur de la ville: a 8 espaces voisins
        if ville[k-2,l-1] == c : 
            effectif = effectif + 1
            total = total + 1
        elif ville[k-2,l-1] != 0 :
            total = total + 1
        if ville[k-2,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l-2] != 0 :
            total = total + 1
        if ville[k-1,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l-2] != 0 :
            total = total + 1
        if ville[k,l-2] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-2] != 0 :
            total = total + 1
        if ville[k,l-1] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k,l-1] != 0 :
            total = total + 1
        if ville[k,l] == c :
            effectif = effectif + 1
            total = total + 1
        elif ville[k,l] != 0 :
            total = total + 1
        if ville[k-1,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-1,l] != 0 :
            total = total + 1
        if ville[k-2,l] == c :
            effectif = effectif + 1 
            total = total + 1
        elif ville[k-2,l] != 0 :
            total = total + 1
            
    #S'il y a bien des habitants autour de l'emplacement (k,l), on calcule la fraction de voisins de 
    #classe différente de c. 
    if total != 0:
        f=1-(effectif/total)
    #Si personne ne vit autour de l'emplacement (k,l), ce dernier n'a aucun voisin de classe
    #différente de c, donc en particulier, donc on a bien f=0. 
    
    return(f)