## importation des module

## declaration des class

class Fleur:
    def __init__(self):
        self.couleur = 'blanc'
        self.taille = 20
        self.nb_petales = 10
        self.nb_feuilles = 0
        
    def affiche_caracteristiques(self):
        print(self.couleur, self.taille, self.nb_petales, self.nb_feuilles)
        
    def ajoute_petale(self):
        self.nb_petales += 1
    
    def enleve_petale(self):
        self.nb_petales -= 1
    
    def allonge(self, x):
        if x > 0:
            self.taille +=  x
        else:
            print(' le paramètre doit être positif ou nul')
    
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
    fleur_2 = Fleur()
    fleur_3 = Fleur()
    
    fleur_2.couleur = 'rouge'
    fleur_2.nbr_petales = 8
    bouquet = [fleur_1, fleur_2, fleur_3]
    for i in bouquet:
        i.affiche_caracteristiques()
    

## programme principal
if __name__ == '__main__':
    main()
