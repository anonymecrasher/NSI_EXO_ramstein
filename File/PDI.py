## importation des module

## declaration des fonction

## declaration des class
class Pile:
    def __init__(self):
        self.valeurs = ()
    
    def est_vide(self):
        return self.valeurs == ()
    
    def empiler(self, valeur):
        self.valeurs = self.valeurs + (valeur,)
    
    def depiler(self):
        if self.est_vide():
            print('la liste est vide')
        sort = self.valeurs[-1]
        self.valeurs = self.valeurs[:-1]
        return sort
    def sommet(self):
        if self.est_vide():
            print('la liste est vide')
        return self.valeurs[-1]
    
    def longeur(self):
        p = Pile()
        i = 0
        while not self.est_vide():
            p.empiler(self.depiler())
            i += 1
        while not p.est_vide():
            self.empiler(p.depiler())
        return i
    
    def tuple(self):
        if self.est_vide():
            print('la liste est vide')
        return self.valeurs
    
## fonction principal
def main():
    pile_1 = Pile()
    print(pile_1.est_vide())
    pile_1.empiler(1)
    pile_1.depiler()
    print(pile_1.est_vide())
    pile_1.empiler(1)
    print(pile_1.depiler())
    pile_1.empiler(1)
    print(pile_1.sommet())
    print(pile_1.longeur())
    pile_1.empiler(1)
    print(pile_1.longeur())
    print(pile_1.tuple())
    
## programme principal
if __name__ == '__main__':
    main()
    