# On définit ici différents tests unitaires pour vérifier le fonctionnement des fonctions principales 
    
import unittest
import numpy as np

from classes import Ville, Paramètres
from grauwin import init_ville, actualise


class Test(unittest.TestCase) :
    
    #Test de la fonction init_ville : 
    #On vérifie que la ville créée par init_ville pour 4 quartiers de 9 emplacements, contient bien 18 individus
    def test_init_ville(self):
        p=Paramètres(2,3,1,1)
        ville = init_ville(p)   
        self.assertEqual(np.sum(ville.ville),18)
    
    #Test de la fonction actualise :
    #On s'assure que :
    #   - la fonction ne modifie pas la ville,
    #   - ou qu'elle ne modifie que deux cases de la ville, qu'elle maintien une densité globale de 1/2, et que les densités par quartiers sont correctes. 
    # On prend l'exemple d'une ville de 4 quartiers de 9 emplacements
    def test_actualise(self):
        p=Paramètres(2,3,1,0.5)
        ville = init_ville(p) 
        ville2 = ville
        actualise(ville2,p)
        test = 1
        for i in range(p.l) :
            for j in range(p.l) :
                if ville.ville[i,j] != ville2.ville[i,j] :
                    test = 0
        if not(test) :
            test = np.sum(ville2.ville) == 18
            
            differences = [[0 if ville.ville[i,j] == ville2.ville[i,j] else 1 for i in range(12)] for j in range(12)]
            test = (test and (np.sum(differences) == 2))
            
            for i in range(2) :
                for j in range(2) :
                    d = np.sum(ville2.ville[i*3 : (i+1)*3-1 , j*3 : (j+1)*3-1])
                    test = (test and ( (d/9) == ville2.densites[i,j] ))           
        self.assertEqual(test,True)
        
        
if __name__ == '__main__':
    unittest.main()   

