# On définit ici différents tests unitaires pour vérifier le fonctionnement des fonctions principales 
    
import unittest
import numpy as np

from classes import Ville, Paramètres
from grauwin import init_ville, actualise
            


class Test(unittest.TestCase) :
    
    #Test de la fonction init_ville : 
    #On vérifie que la ville créée par init_ville pour 4 quartiers de 9 emplacements, contient bien 18 individus
    def test_init_ville(self):
        p=Paramètres(2,3,1,0.5,0.2)  
        ville = init_ville(p)
        n_al = 0  #nombre de personnes altruistes : normalement 3
        n_eg = 0  #nombre de personnes égoïstes : normalement 15
        for i in range(p.l) :
            for j in range(p.l) :
                if ville.ville[i,j] == 1 :
                    n_eg+=1
                elif ville.ville[i,j] == 2 :
                    n_al+=1
        self.assertEqual([n_eg,n_al],[15,3])
        
    #Test de la fonction actualise :
    #On s'assure qu'elle ne modifie que deux cases de la ville, que le nombre d'individus égoistes et altruistes est toujours correcte, et que les densités par quartiers sont correctes. 
    # On prend l'exemple d'une ville de 4 quartiers de 9 emplacements
    def test_actualise(self):
        p=Paramètres(4,5,100,0.2,0.1)  #Une grande valeur de T permet d'accélérer les déménagements
        ville = init_ville(p) 
        copie_ville = np.copy(ville.ville)  #list permet de faire une copie indépendante 
        copie_densites = np.copy(ville.densites)
        ville2 = Ville(copie_ville,copie_densites)
        
        test = True
        while test :  #on réactualise la ville jusqu'à ce qu'un déménagement ait lieu
            actualise(ville2,p)
            for i in range(p.l) :
                for j in range(p.l) :
                    if ville.ville[i,j] != ville2.ville[i,j] :
                        test = False
            #A ce stade, test vaut 1 si la ville est inchangée, et 0 sinon
        
        # Vérification de la grille de la ville :
        n_al = 0  #nombre de personnes altruistes : normalement 3
        n_eg = 0  #nombre de personnes égoïstes : normalement 15
        n_change = 0 #nombre de changements entre ville et ville2
        for i in range(20) :
            for j in range(20) :
                if ville2.ville[i,j] == 1 :
                    n_eg+=1
                elif ville2.ville[i,j] == 2 :
                    n_al+=1  
                if ville.ville[i,j] != ville2.ville[i,j] :
                    n_change += 1
        test = (n_eg == 180) and (n_al == 20) and (n_change == 2) #vérifie qu'il y a bien le bon nombre d'individus altruistes et égoistes, et que seules deux cases de la ville ont été modifiées

        #Vérification de la matrice des densités :
        for i in range(4) :
            for j in range(4) :
                d = np.sum(ville2.ville[i*5 : (i+1)*5-1 , j*5 : (j+1)*5-1]!=0)
                test = (test and ( (d/25) == ville2.densites[i,j] ))   #vérifie que les densités sont bonnes         
        self.assertEqual(test,True)
            
        
        
if __name__ == '__main__':
    unittest.main()   

