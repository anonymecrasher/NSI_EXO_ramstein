## Importation des modules

## declaration des consante

## Déclaration des fonctions

## Déclaration des classes
class Graph_oriente():
    def __init__(self, ordre:int):
        self.ordre = ordre
        self.listes_successeurs = {}
        self.listes_predecesseurs = {}
        for i in range(self.ordre):
            self.listes_successeurs[f'{i}'] = {}
            self.listes_predecesseurs[f'{i}'] = {}
        
    def ajouter_arc(self,a,b,v=1):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.listes_successeurs[str(a)][str(b)] = v
        self.listes_predecesseurs[str(b)][str(a)] = v
            
    def suprrimer_arc(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.listes_successeurs[str(a)].pop(str(self.listes_successeurs[str(a)][str(b)]))
        self.listes_predecesseurs[str(b)].pop(str(self.listes_predecesseurs[str(b)][str(a)]))
            
    def sont_adjacents(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        return self.listes_successeurs[str(a)][str(b)] != 0 and self.listes_predecesseurs[str(b)][str(a)] != 0
    
    def succeseurs(self,a):
        return self.listes_successeurs[str(a)]
    
    def predecesseurs(self,a):
        return self.listes_predecesseurs[str(a)]
    
    def ajouter_sommet(self, a):
        self.ordre += 1
        self.listes_successeurs[str(a)] = {}
        self.listes_predecesseurs[str(a)] = {}
        
    def supprimer_sommet(self,a):
        del(self.listes_successeurs[str(a)])
        del(self.listes_predecesseurs[str(a)])
        self.ordre -=1
        
class Graph_non_oriente():
    def __init__(self, ordre:int):
        self.ordre = ordre
        self.listes_successeurs = {}
        self.listes_predecesseurs = {}
        for i in range(self.ordre):
            self.listes_successeurs[f'{i}'] = {}
            self.listes_predecesseurs[f'{i}'] = {}

    def ajouter_arete(self,a,b,v=1):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.listes_successeurs[str(a)][str(b)] = v
        self.listes_predecesseurs[str(b)][str(a)] = v
        self.listes_successeurs[str(b)][str(a)] = v
        self.listes_predecesseurs[str(a)][str(b)] = v
            
    def suprrimer_arc(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.listes_successeurs[str(a)].pop(str(self.listes_successeurs[str(a)][str(b)]))
        self.listes_predecesseurs[str(b)].pop(str(self.listes_predecesseurs[str(b)][str(a)]))
        self.listes_successeurs[str(b)].pop(str(self.listes_successeurs[str(b)][str(a)]))
        self.listes_predecesseurs[str(a)].pop(str(self.listes_predecesseurs[str(a)][str(b)]))
            
    def sont_adjacents(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        return self.listes_successeurs[str(a)][str(b)] != 0 and self.listes_predecesseurs[str(b)][str(a)] != 0 and self.listes_successeurs[str(b)][str(a)] != 0 and self.listes_predecesseurs[str(b)][str(a)] != 0
    
    def succeseurs(self,a):
        return self.listes_successeurs[str(a)]
    
    def predecesseurs(self,a):
        return self.listes_predecesseurs[str(a)]
    
    def ajouter_sommet(self, a):
        self.ordre += 1
        self.listes_successeurs[str(a)] = {}
        self.listes_predecesseurs[str(a)] = {}
        
    def supprimer_sommet(self,a):
        del(self.listes_successeurs[str(a)])
        del(self.listes_predecesseurs[str(a)])
        self.ordre -=1
        
        

## fonction principale
def main():
    g = Graph_oriente(5)
    g.ajouter_sommet(6)
    g.ajouter_arc(0, 1)
    print(g.listes_successeurs)
    g.supprimer_sommet(1)
    print(g.listes_successeurs)
    

## programme principal
if __name__ == '__main__':
    main()
