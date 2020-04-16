# Dans ce programme, on cherche à vérifier le coût d'execution estimé d'une simulation suivant le modèle de Grauwin et Jensen.



from classes import Paramètres
from grauwin import grauwin, init_ville

from time import time  
from math import log
import matplotlib.pyplot as plt 

from sklearn.linear_model import LinearRegression



# Le temps d'execution ne dépendant que de h, q et n_iter, on fixe des paramètres T, m et alpha quelconques.
T = 1
m = 0.2
alpha = 0.2



# Commençons par étudier le lien entre temps d'éxecution et nombre d'itérations n_iter du modèle : on fixe q et h, et on trace le temps d'execution en fonction de n_iter. On s'attend à observer une droite affine de type t = a*n_iter + b ie que t = O(n_iter). On vérifie en effectuant une régression linéaire et en observant le coefficient r² associé. 

def cout_n_iter () :
    h = 10
    q = 5
    x=[]  #contient les différentes valeurs de n_iter testées
    y=[]  #contient le temps d'execution associé
    for n_iter in range(1,5000,5) :
        p = Paramètres(q,h,T,m,alpha)
        x.append(n_iter)
        t=time()
        grauwin(p,n_iter)
        t=time()-t
        y.append(t) 
    #Réalisons ensuite une régression linéaire pour trouver a et b tels que t = a*n_iter + b :
    regressor = LinearRegression()
    X = [[i] for i in x]
    regressor.fit(X, y)
    a = regressor.coef_[0]
    b = regressor.intercept_
    r2 = regressor.score(X,y)
    y_droite = [a*i + b for i in x]
    #On trace ensuite les points obtenus en effectuant les simulations, et la droite obtenue par régression linéaire. 
    plt.plot(x,y, label = "t(n_iter)")
    plt.plot(x,y_droite, label = "t="+str(a)+"n_iter+"+str(b)+", r² ="+str(r2))
    plt.title("Temps d'exécution t en fonction du nombre d'itérations n_iter (1000 points)")
    plt.xlabel("n_iter")
    plt.ylabel("t (en secondes)")
    plt.legend()
    plt.show()

#cout_n_iter()
    
    

# Essayons désormais d'étudier la dépendance en q et h du temps d'exécution. On fixe donc un nombre d'exécutions n_iter quelconque. Comme on s'attend à des temps d'exécution en O(h²) et O(q²), on essaye de tracer ln(t) en fonction de ln(q) et ln(h)
#Ici, j'ai substitué grauwin par init_ville car on a établit que la dépendance du temps d'éxécution en q et h n'intervient que dans cette fonction. Appeler grauwin a le double inconvénient d'augmenter inutilement le temps d'exécution des algorithmes suivants, et de rendre le calcul moins précis en ajoutant de nombreux pics dus au choix d'individus et d'emplacements vides aléatoires réalisés dans grauwin.

def cout_q () :   
    h = 20
    x=[]  #contient les différentes valeurs de h testées
    y=[]  #contient le temps d'execution associé
    for q in range(1,51) :
        p = Paramètres(q,h,T,m,alpha)
        x.append(log(q))
        t=time()
        init_ville(p)   
        t=time()-t
        y.append(log(t))
    #Réalisons ensuite une régression linéaire pour trouver a et b tels que log(t) = a*log(h) + b :
    regressor = LinearRegression()
    X = [[i] for i in x]
    regressor.fit(X, y)
    a = regressor.coef_[0]
    b = regressor.intercept_
    r2 = regressor.score(X,y)
    y_droite = [a*i + b for i in x]
    #On trace ensuite les points obtenus en effectuant les simulations, et la droite obtenue par régression linéaire. 
    plt.plot(x,y, label = "log(t) en fonction de log(q)")
    plt.plot(x,y_droite, label = "log(t)="+str(a)+"log(q)+"+str(b)+", r² ="+str(r2))
    plt.title("Temps d'exécution t en fonction du nombre de quartiers q² (50 points)")
    plt.xlabel("log(q)")
    plt.ylabel("log(t) (t en secondes)")
    plt.legend()
    plt.show()

#cout_q()
    

def cout_h () :  #Même fonction que cout_q en remplaçant q par h
    q = 5
    x=[]  #contient les différentes valeurs de h testées
    y=[]  #contient le temps d'execution associé
    for h in range(10,101) :   #on enlève les petites valeurs pour ne pas avoir un temps trop petit (et un problème lors du passage au log)
        p = Paramètres(q,h,T,m,alpha)
        x.append(log(h))
        t=time()
        init_ville(p)
        t=time()-t
        y.append(log(t))
    #Réalisons ensuite une régression linéaire pour trouver a et b tels que log(t) = a*log(h) + b :
    regressor = LinearRegression()
    X = [[i] for i in x]
    regressor.fit(X, y)
    a = regressor.coef_[0]
    b = regressor.intercept_
    r2 = regressor.score(X,y)
    y_droite = [a*i + b for i in x]
    #On trace ensuite les points obtenus en effectuant les simulations, et la droite obtenue par régression linéaire. 
    plt.plot(x,y, label = "log(t) en fonction de log(h)")
    plt.plot(x,y_droite, label = "log(t)="+str(a)+"log(h)+"+str(b)+", r² ="+str(r2))
    plt.title("Temps d'exécution t en fonction du nombre d'emplacements par quartiers h² (90 points)")
    plt.xlabel("log(h)")
    plt.ylabel("log(t) (t en secondes)")
    plt.legend()  
    plt.show()

#cout_h()


