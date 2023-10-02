## importation des module

## declaration des class

class Fleur:
    def __init__(self, couleur='blanc', taille=20, nb_petales=10, nb_feuilles=0):
        self.couleur = couleur
        self.taille = taille
        self.nb_petales = nb_petales
        self.nb_feuilles = nb_feuilles
        self.affiche_caracteristiques()
        
    def affiche_caracteristiques(self):
        print(self.couleur, self.taille, self.nb_petales, self.nb_feuilles)
        
    def ajoute_petale(self):
        self.nb_petales += 1
    
    def enleve_petale(self):
        if self.nb_petales > 0:
            self.nb_petales -= 1
    
    def allonge(self, x):
        assert x > 0, 'le paramètre doit être positif ou nul'
        
        self.taille +=  x
    
    
    def pousse(self):
        self.taille *= 1.1
        self.taille = round(self.taille)
    
    def est_fanee():
        if self.nb_petales > 0:
            return False
        else:
            return True
    
        


## declaration des fonction
        
        
        


def main():
    fleur_1 = Fleur()
    fleur_2 = Fleur(taille=30)
    fleur_3 = Fleur()
    
    fleur_2.couleur = 'rouge'
    fleur_2.nbr_petales = 8
    bouquet = [fleur_1, fleur_2, fleur_3]
    fleur_1.allonge(999)
    

## programme principal
if __name__ == '__main__':
    main()
