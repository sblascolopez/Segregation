# Il a été difficile pour moi de trouver les fonctions adéquates pour pouvoir représenter une ville.


# J'avais tout d'abord penser à utiliser la fonction FuncAnimation de la librairie matplotlib.pyplot, que j'avais déjà utiliser pour faire une animation avec des nuages de points.
# Je n'ai cependant pas réussi à adapter son utilisation, l'argument étant une grille et non pas un nuage de point ou une courbe. 


# J'ai donc cherché à représenter "manuellement la grille", tout d'abord à l'aide de "patch", en utilisant la fonction Rectangle de matplotlib.pyplot.plot : 

from classes import Ville, Paramètres
from grauwin import init_ville, actualise

import matplotlib.pyplot as plt 


#Ppremière fonction qui trace le fond, c'est à dire les frontières de la ville et des quartiers

def init_figure (p,i) :   # i est le numéro de la figure
    fig = plt.figure(i)
    ax = plt.axes(xlim=(0, p.l), ylim=(0, p.l))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect("equal")
    #On trace chacune des frontières des quartiers :
    for i in range(1,p.q) :
        plt.axvline(x=i*p.h,color='black')
        plt.axhline(y=i*p.h,color='black')


#Ensuite, on écrit une fonction qui représente une ville    
    
def dessine_ville (ville, p) :
    for i in range(p.l):
        for j in range(p.l) :
            if ville.ville[i,j]==1 :
                rect = plt.Rectangle((i,j),1,1, fill=True, color='red')
                ax.add_patch(rect)
            elif ville.ville[i,j]==2 :
                rect = plt.Rectangle((i,j),1,1, fill=True, color='green')
                ax.add_patch(rect) 


# Le but étant d'utiliser la fonction suivante pour réaliser une simualation :

def simulation (p,i_max,nb_graph) :  #choisis de sorte que i_max divisible par (nb_graph-1)
    ville = init_ville(p)
    init_figure(p,0)
    dessine_ville(ville,p)
    plt.draw()
    sub_i = i_max // (nb_graph-1)   # Nombre d'itérations entre chaque graphique
    for i in range(1,nb_graph) :
        for j in range(sub_i) :
            actualise(ville,p)
        init_figure(p,i)
        dessine_ville(ville,p)
        plt.draw()                
 
    
# Ici, le problème est que la fonction dessine_ville ne reconnait pas "ax", je ne sais pas comment bien gérer les figures et leurs caractéristiques sur Python. Peut être aurait-il fallu regrouper toutes ces fonctions en une pour ne pas avoir ce problème. C'est ce que j'ai essayé de faire dans la fonction trace_ville finale.

# J'ai cherché à utiliser d'autres fonctions de Python, afin de ne pas avoir à dessiner chaque rectangle manuellement, et de trouver une solution pour afficher une animation. Je ne parvenais en effet à n'afficher qu'une seule image à chaque fois, les autres ne s'affichaient pas dans ma console. 
# J'ai pour cela fait appel à un ami développeur qui a beaucoup plus de connaissances et d'expérience que moi en Python. Il m'a suggéré d'essayer d'utiliser les fonctions grid et imshow de matplotlib.pyplot. Je ne parvenais pas à avoir comme lui une actualisation de l'animation (peut-être le problème vient il de ma propre console), mais en numérotant les figures je suis parvenue à afficher successivement chaque graphique, ce qui me convient pour l'utilisation que je veux en faire.

    





