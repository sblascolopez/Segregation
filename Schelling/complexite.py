#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:10:18 2020

@author: victorhuynh
"""

from time import time
from sklearn.linear_model import LinearRegression

from simulationdebase import schelling

def cout_n_iter () :
    P = Paramètre(50,80,1/2)
    x=[]  #Contiendra les différentes valeurs de n_iter testées.
    y=[]  #Contiendra le temps d'execution associé.
    for n_iter in range(1,5000,5) :
        x.append(n_iter)
        t=time() #t prend pour valeur l'heure avant simulation.
        schelling(P,n_iter) 
        #On effectue une simulation avec n_iter itérations et les autres paramètres choisis.
        t=time()-t 
        #t prend pour valeur la différence entre l'heure avant la simulation et après, 
        #c'est-à-dire le temps que prend la simulation.
        y.append(t)
    #Réalisons ensuite une régression linéaire pour trouver a et b tels que t = a*n_iter + b :
    regressor = LinearRegression()
    X = [[i] for i in x]
    #Liste constituée de listes unitaires contenant chacun des éléments de x. 
    regressor.fit(X, y)
    #On effectue la régression linéaire
    a = regressor.coef_[0]
    b = regressor.intercept_
    r2 = regressor.score(X,y)
    y_droite = [a*i + b for i in x] #On constitue la droite de régression linéaire.
    #On trace ensuite les points obtenus en effectuant les simulations, 
    # et la droite obtenue par régression linéaire. 
    axes = plt.gca()
    axes.set_xlim(0,5000)
    plt.plot(x,y, label = "t(n_iter)")
    plt.plot(x,y_droite, label = "t="+str(a)+"n_iter+"+str(b)+", r² ="+str(r2))
    plt.title("Temps d'exécution t en fonction du nombre d'itérations n_iter (1000 points)")
    plt.xlabel("n_iter")
    plt.ylabel("t (en secondes)")
    plt.legend()
    plt.show()