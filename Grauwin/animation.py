# On crée ici des fonctions permettant de réaliser et de modéliser une simulation 

from classes import Ville, Paramètres
from grauwin import init_ville, actualise

import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation


#Commençons par une première fonction qui trace le fond, c'est à dire les frontières de la ville et des quartiers
def init_figure (p) :
    fig = plt.figure()
    ax = plt.axes(xlim=(0, p.l), ylim=(0, p.l))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect("equal")
    #On trace chacune des frontières des quartiers :
    for i in range(1,p.q) :
        plt.axvline(x=i*p.h,color='black')
        plt.axhline(y=i*p.h,color='black')
    plt.show()
 
    
    
#Test :
    
p=Paramètres(4,5,1,0.5)
init_figure(p)
