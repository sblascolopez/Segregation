# On crée ici un programme permettant de réaliser et de visualiser une simulation 


from classes import Ville, Paramètres
from grauwin import init_ville, actualise

import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation



#Commençons par une fonction qui représente une ville donnée en arguments

def trace_ville (ville,p,i) :  # i est le numéro de la figure
    
    #On initialise la figure et on règle les axes :
    fig = plt.figure(i)
    ax = plt.axes(xlim=(-0.5, p.l-0.5), ylim=(-0.5, p.l-0.5))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect("equal")
    
    #On trace chacune des frontières des quartiers :
    for i in range(1,p.q) :
        plt.axvline(x=i*p.h-0.5,color='black')
        plt.axhline(y=i*p.h-0.5,color='black')
    
    #On place ensuite les individus :
    cmap = ListedColormap([(1,1,1),(1,0,0),(0,1,0)])
    img = plt.imshow(ville.ville, cmap=cmap)
    plt.draw()


#Ensuite, on crée une fonction qui réalise la simulation, et affiche l'état de la ville à intervalle de temps régulier.
#On lui donne en argument les paramètres, le nombre d'itérations et le nombre de graphiques souhaités

def simulation (p,i_max,nb_graph) :  #choisis de sorte que i_max divisible par (nb_graph-1)
    ville = init_ville(p)
    trace_ville(ville,p,0)
    sub_i = i_max // (nb_graph-1)   # Nombre d'itérations entre chaque graphique
    for i in range(1,nb_graph) :
        for j in range(sub_i) :
            actualise(ville,p)
        trace_ville(ville,p,i)
    
    
    
#Enfin, afin de faciliter la prise en main du programme, on crée une fonction qui est appelée quand on exécute le programme, et qui demande à l'utilisateur les différents paramètres de la simulation qu'il souhaite effectuer

def realise_simulation () :
    q = int(input("Racine q du nombre de quartiers (il y aura Q=q² quartiers) : "))
    h = int(input("Racine h du nombre d'emplacements par quartier (il y aura H=h² quartiers) : "))
    T = float(input("Paramètre T représentant les contraintes des individus s'opposant à leur déménagement :"))
    m = float(input("Utilité m d'habiter dans un quartier complètement rempli (0≤m≤1) :"))
    alpha = float(input("Fraction α de la population altruiste :"))
    p = Paramètres(q,h,T,m,alpha)
    i_max = int(input("Nombre i_max d'itérations lors de la simulation :"))
    nb_graph = int(input("Nombre n de graphes souhaités (tel que i_max soit divisible par n-1) :"))
    simulation(p,i_max,nb_graph)


realise_simulation()

plt.show()



#Test
#       
#p=Paramètres(5,10,0.1,0,0.2)
#
#simulation(p,8000,5)
#           
#plt.show()