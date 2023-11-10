# importation des module

# declaration des fonction

# declaration des class
class Maillon():
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant
        

class Liste_chainee():
    def __init__(self, tete=None):
        self.tete = tete
        
    def est_vide(self):
        return self.tete == None
    def ajouter_element_queue(self, valeur=0):
        
        

# fonction principal
def main():
    l1 = Liste_chainee()

# programme principal
if __name__ == '__main__':
    main()