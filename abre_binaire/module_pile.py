## Importation des modules


## Déclaration des classes

class Pile:
    def __init__(self):
        self.valeurs = ()
        
    def est_vide(self):
#         if self.valeurs == ():
#             return True
#         else:
#             return False
        
        return self.valeurs == ()
    
    def empiler(self, valeur):
        self.valeurs = self.valeurs + (valeur,)
    
    def depiler(self):
        if self.est_vide() == False:
            derniere_valeur = self.valeurs[-1]
            self.valeurs = self.valeurs[0:-1]
            
            return derniere_valeur

    def sommet(self):
        if self.est_vide() == False:
            return self.valeurs[-1]
        
    def longueur(self):
        if self.est_vide() == True:
            return 0
        else:
            pile_temporaire = Pile()
            i = 0
            while self.est_vide() == False:
                pile_temporaire.empiler(self.depiler())
                i = i + 1
            
            while pile_temporaire.est_vide() == False:
                self.empiler(pile_temporaire.depiler())            
                
        return i
    
    def tuple(self):
        return self.valeurs


## Déclaration des fonctions


## Programme principal
