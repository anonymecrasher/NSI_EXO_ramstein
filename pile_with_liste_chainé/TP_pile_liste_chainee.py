## importation des module
import m_l_c

## declaration des fonction

## declaration des class
class Pile:
    def __init__(self):
        self.valeurs = m_l_c.Liste_chainee()
        
    def est_vide(self):
        return self.valeurs.est_vide()
    
    def empiler(self, valeur):
        self.valeurs.ajouter_element_queue(valeur)
        
    def depiler(self):
        dernier_valeur = self.valeurs.extrait_element(self.valeurs.longueur() - 1) 
        self.valeurs.supprimer_element_queue(valeur)
        return dernier_valeur
    
    def sommet(self):
        return self.valeurs.extrait_element(self.valeurs.longueur() - 1)
    
    def longueur(self):
        return self.valeurs.longueur()
    
    def tuple(self):
        return self.valeur.list()
        
        
        
    
## fonction principal
def main():
    pass
    
## programme principal
if __name__ == '__main__':
    main()