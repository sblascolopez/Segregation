#Dans ce programme, on fixe arbitrairement h=10 et q=5, ainsi que alpha=0 et n_iter=1000, et on étudie l'état de la ville en faisant varier T et m 


from classes import Paramètres
from grauwin import grauwin

import matplotlib.pyplot as plt 
import seaborn as sns


h = 10
q = 5
n_iter = 5000
alpha = 0


#Etudions dans un premier temps l'effet de la variation de T : pour quelques valeurs de T choisies, on réalise de nombreuses simulations et on garde en mémoire les différentes densites obtenus dans les quartiers de la ville. On réalise ensuite un histogramme de ces valeurs.

def analyse_T () :
    m = 0.2  # valeur de m quelconque
    T = [0.01,0.2,0.5,1,20,100]  # Diféérentes valeurs de T que nous allons tester
    for k in range(6) :
        p = Paramètres(q,h,T[k],m,alpha)
        fig = plt.figure(k)
        densites_finales = [] # Densités obtenues
        for l in range(200) :  # On réalise 200 simulations, on aura donc 7200 densités
            densites = grauwin(p,n_iter).densites
            for i in range(q):
                for j in range(q) :
                    densites_finales.append(densites[i,j])
        sns.distplot(densites_finales, axlabel = "densités de quartiers")
        plt.title("Densités de quartiers obtenues après 200 simulations (7200 densités) avec T="+str(T[k]))
        plt.draw()

#analyse_T()


# De la même manière, étudions l'effet des variations de m, pour de petites valeurs de T
        
def analyse_m() :
    T = [0.01, 0.2, 100]
    m = [0, 0.2, 0.4, 0.6, 0.8]  # Diféérentes valeurs de m que nous allons tester
    for k in range(3) :  # indice de la valeur de T
        fig=plt.figure(k)
        for l in range(5) :  # indice de la valeur de m
            p = Paramètres(q,h,T[k],m[l],alpha)
            densites_finales = []
            for n in range(200) :  # On réalise 200 simulations, on aura donc 7200 densités
                densites = grauwin(p,n_iter).densites
                for i in range(q):
                    for j in range(q) :
                        densites_finales.append(densites[i,j])
            sns.distplot(densites_finales, axlabel = "densités de quartiers", label = "m="+str(m[l]), hist = False)
        plt.title("Densités de quartiers obtenues après 200 simulations (7200 densités) pour différentes valeurs de m, avec T="+str(T[k]))
        plt.legend()
        plt.draw()

#analyse_m()
            
        
