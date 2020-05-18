#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:55:04 2020

@author: victorhuynh
"""


class Paramètre : #Cas de base
    """ Classe regroupant tous les paramètres de la ville """
    
    def __init__ (self,n,p,T) :
        self.n = n
        self.p = p 
        # n et p définissent les paramètres de longueur et largeur de la ville.

        self.T = T # Seuil de tolérance des individus
        
        
class Paramètre2 : #Cas où l'on différentie les seuils de tolérance par ethnie
    
    def __init__ (self,n,p,Tb,Tn) :
        self.n = n
        self.p = p 

        self.Tb = Tb # Seuil de tolérance des individus blancs
        self.Tn = Tn # Seuil de tolérance des individus noirs
        
class Paramètre3 : #Cas où l'on souhaite décider des proportions ethniques, pour 2 ethnies
    
    def __init__ (self,n,p,T,proportion_vides,proportion_blancs,proportion_noirs) :
        self.n = n
        self.p = p 
        # n et p définissent les paramètres de longueur et largeur de la ville.

        self.T = T # Seuil de tolérance des individus 
        self.proportion_vides = proportion_vides
        self.proportion_blancs = proportion_blancs
        self.proportion_noirs = proportion_noirs
        
        
class Paramètre4 : #Cas où l'on souhaite décider des proportions ethniques, pour 2 ethnies
    
    def __init__ (self,n,p,T,proportion_vides,proportion_blancs,proportion_noirs,proportion_asiats,proportion_latinos) :
        self.n = n
        self.p = p 
        # n et p définissent les paramètres de longueur et largeur de la ville.

        self.T = T # Seuil de tolérance des individus 
        self.proportion_vides = proportion_vides
        self.proportion_blancs = proportion_blancs
        self.proportion_noirs = proportion_noirs
        self.proportion_asiats = proportion_asiats
        self.proportion_latinos = proportion_latinos
