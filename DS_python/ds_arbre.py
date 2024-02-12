## importation des module

## declaration des fonction

        
def parcours_infixe(arbre):
    """
    @input: arbre
    @output: une liste
    renvoie une liste de valeur de l'abre en suivant le parcours_infixe
    """
    if arbre == None:
        return []
    else:
        gauche = parcours_infixe(arbre.gauche)
        val = [arbre.valeur]
        
        droit = parcours_infixe(arbre.droit)
        
        return gauche+val+ droit

def parcours_prefixe(arbre):
    """
    @input: arbre
    @output: une liste
    renvoie une liste de valeur de l'abre en suivant le parcours_prefixe
    """
    if arbre == None:
        return []
    else:
        val = [arbre.valeur]
        
        gauche = parcours_prefixe(arbre.gauche)
        droit = parcours_prefixe(arbre.droit)
        
        return val+gauche+ droit
    
def parcours_sufixe(arbre):
    """
    @input: arbre
    @output: une liste
    renvoie une liste de valeur de l'abre en suivant le parcours_sufixe
    """
    if arbre == None:
        return []
    else:
        gauche = parcours_sufixe(arbre.gauche)
        droit = parcours_sufixe(arbre.droit)
        val = [arbre.valeur]
        
        
        return gauche+ droit+val
    
def liste_ordre_croissant(liste):
    re = True
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            re = False
            
    return re
        


    
        
## declaration des classe
class Arbre:
    def __init__(self, valeur, gauche= None, droit= None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
    def inserer(self, valeur):
        """
        @input: a
        @input: valeur
        insere la valeur dans a en suivant les relge des arbre binaire
        """
        
        if valeur < self.valeur:
            if self.gauche == None:
                self.gauche= Arbre(valeur)
            else:
                self.gauche.inserer(valeur)
            
        else:
            if self.droit == None:
                self.droit= Arbre(valeur)
            else:
                self.droit.inserer(valeur)
            
    def minimum(self):
        """
        renvoie la valeur minimal de l'arbre
        """
        if self.gauche is None:
            return self.valeur
        return self.gauche.minimum()
    
    def maximum(self):
        """
        renvoie la valeur maximal de l'arbre
        """
        if self.droit is None:
            return self.valeur
        return self.droit.maximum()
    

## fonction principal
def main():
    a = Arbre(1)
    a.droit = Arbre(4)
    a.gauche = Arbre(8)
    a.droit.droit = Arbre(7)
    a.inserer(9)
    #utiliser minimum
    print(a.minimum())
    print(liste_ordre_croissant(parcours_infixe(a)))
    
    print(a.droit.droit.droit.valeur)
## programme principal
if __name__ == '__main__':
    main()
