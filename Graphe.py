## Importation des modules

## declaration des consante

## Déclaration des fonctions

## Déclaration des classes
class Graph_oriente():
    def __init__(self, ordre:int,etiquete):
        self.ordre = ordre
        temp = ordre*[0]
        self.matrice = [temp.copy() for i in range(ordre)]
        self.etiquete = etiquete
        
    def ajouter_arc(self,a,b,v=1):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.matrice[a][b] = v
            
    def suprrimer_arc(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        self.matrice[a][b] = 0
            
    def sont_adjacents(self,a,b):
        assert a < self.ordre and b < self.ordre, 'index out of range'
        return self.matrice[a][b] != 0 or self.matrice[b][a] != 0
    
    def succeseurs(self,a):
        ret = []
        for i in range(self.ordre):
            if self.matrice[a][i]:
                ret.append(i)
        return ret
    def predecesseurs(self,a):
        ret = []
        for i in range(self.ordre):
            if self.matrice[i][a]:
                ret.append(i)
        return ret
    def ajouter_sommet(self):
        for i in range(self.ordre):
            self.matrice[i].append(0)
        self.ordre += 1
        self.matrice.append([0]*self.ordre)
        
    def supprimer_sommet(self,a):
        
        self.matrice.pop(a)
        self.ordre -=1
        
        for i in range(self.ordre):
            self.matrice[i].pop(a)
        

## fonction principale
def main():
    g = Graph_oriente(5,"m'en fou")
    g.ajouter_sommet()
    g.ajouter_arc(0, 1)
    print(g.matrice)
    g.supprimer_sommet(1)
    print(g.matrice)
    

## programme principal
if __name__ == '__main__':
    main()
