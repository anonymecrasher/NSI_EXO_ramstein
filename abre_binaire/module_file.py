## Importation des modules

from module_pile import *
# import module_pile

## Déclaration des classes

class File:
    def __init__(self):
        self.pile_1 = Pile()
        # self.pile_1 = module_pile.Pile()
        self.pile_2 = Pile()
        # self.pile_2 = module_pile.Pile()
        
    def est_vide(self):
        if self.pile_1.est_vide() and self.pile_2.est_vide():
            return True
        else:
            return False
    
    def tuple(self):
        valeurs = ()
        while self.pile_1.est_vide() == False:
            valeurs = valeurs + (self.pile_1.depiler(),)
        while self.pile_2.est_vide() == False:
            self.pile_1.empiler(self.pile_2.depiler())
        while self.pile_1.est_vide() == False:
            valeurs = valeurs + (self.pile_1.depiler(),)
        
        for el in valeurs:
            self.pile_2.empiler(el)
        
        return valeurs

    def longueur(self):
        return self.pile_1.longueur() + self.pile_2.longueur()

    def enfiler(self, valeur):
        self.pile_2.empiler(valeur)
    
    def defiler(self):
        if self.est_vide() == False:
            if self.pile_1.est_vide() == False:
                return self.pile_1.depiler()
            else:
                while self.pile_2.est_vide() == False:
                    self.pile_1.empiler(self.pile_2.depiler())
                return self.pile_1.depiler()


## Déclaration des fonctions


## Programme principal
