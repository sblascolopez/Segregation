# On définit ici deux classes : 
#l'une contenant les paramètres des simulations, 
#l'autre regroupant les caractéristiques d'une ville lors des simulations.


class Paramètres :
    """ Classe regroupant tous les paramètres d'une simulation """
    
    def __init__ (self,q,h,T,m,alpha = 0) :
        self.q = q  # définit le nombre de quartier Q = q²
        self.h = h  # définit le nombre d'emplacements par quartiers H = h²
        self.l = h*q  # taille de la ville 
        
        self.N = ((h*q)**2)/2  # Nombre d'agents initialement 
        self.T = T # Contrainte caractérisant l'ancrage des individus dans leur quartier
        self.alpha = alpha  # Coefficient intégrant l'altruisme
        
        self.u = lambda x : 2*x if x <= 1/2 else (2*(m-1)*x+2-m) # Fonction d'utilité des agents


class Ville :
    """Classe regroupant toutes les caractéristiques de la ville d'une simulation :
        - la ville, sous la forme d'une grille de taille l * l, contenant des 0 si l'emplacement est occupé, des 1 s'il est occupé
        - les densités de chaque quartier, sous la forme d'une grille q*q
    """
    
    def __init__ (self,ville,densites) :
        self.ville = ville
        self.densites = densites
        

#On peut également définir la fonction d'utilité agrégée :
        
def U(ville,p) :
    s = 0
    for i in range(p.q) :
        for j in range(p.q) :
            rho = ville.densites[i,j]
            s+= rho * p.u(rho)
    H = (p.h)**2
    return s * H
            
