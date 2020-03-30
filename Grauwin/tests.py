# On définit ici différents tests unitaires pour vérifier le fonctionnement des fonctions principales 
    
import unittest
import numpy as np

from classes import Ville, Paramètres
from grauwin import init_ville


class Test(unittest.TestCase) :
    
    #Test de la fonction init_ville : 
    #On vérifie que la ville créée par init_ville pour 4 quartiers de 9 emplacements, contient bien 18 individus
    def test_init_ville(self):
        p=Paramètres(2,3,1,1)
        ville = init_ville(p)   
        self.assertEqual(np.sum(ville.ville),18)
        
if __name__ == '__main__':
    unittest.main()   

