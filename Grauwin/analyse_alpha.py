#Dans ce programme, on fixe arbitrairement h=10, q=5, ainsi que T=0.01, m=0.2 et n_iter=1000, et on étudie l'état de la ville en fonction de la proportion de personnes bienveillantes ajoutées


from classes import Paramètres
from grauwin import grauwin
from simulation import simulation

import matplotlib.pyplot as plt 
import seaborn as sns



h = 10
q = 5
T = 0.01
m = 0.2



# Simulation 1 : sans agents bienveillants, conduisant à une ségrégation :

#p=Paramètres(q,h,T,m,alpha=0)
#simulation(p,35000,8)  # On réalise 8 graphiques, chacun espacés de 5000 itérations       
#plt.show()



# Simulation 2 : avec agents bienveillants

#p=Paramètres(q,h,T,m,alpha=0.15)
#simulation(p,35000,8)  # On réalise 8 graphiques, chacun espacés de 5000 itérations         
#plt.show() 



# Pour évaluer de alpha, on réalise plusieurs histogrammes en faisant varier la proportion d'agents altruistes au sein de la ville

def analyse_alpha () :
    alpha = [0.2, 0.15, 0.1, 0.05, 0]  # Différentes valeurs de alpha que nous allons tester (on s'arrête à 20% car les altruistes sont censés restés très minoritaires dans ce modèle). 
    # Elles sont classées dans l'ordre décroissant car les pics des courbes sont plus hauts pour les grandes valeurs de alpha, et l'axe des ordonnées doit être créé par rapport à ces pics.
    for k in range(5) :
        p = Paramètres(q,h,T,m,alpha[k])
        densites_finales = [] # Densités obtenues
        for l in range(100) :  # On réalise 200 simulations, on aura donc 3600 densités
            densites = grauwin(p,20000).densites
            for i in range(q):
                for j in range(q) :
                    densites_finales.append(densites[i,j])
        sns.distplot(densites_finales, axlabel = "densités de quartiers", label = "alpha = "+str(alpha[k]), hist=False)
    plt.title("Densités de quartiers obtenues après 100 simulations (3600 densités)")
    plt.legend()

#analyse_alpha()
#plt.show()
        