## importation des module

## declaration des fonction

## declaration de class
class labyrinthe:
    def __init__(self, tab):
        self.tab = tab
        
    def afficher(self):
        return self.tab
        
    def nb_ligne(self):
        return len(self.tab)
        
    def nb_colone(self):
        return len(self.tab[0])
    
    def depart(self):
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                if self.tab[x][y] == 2:
                    return x,y
                
    def arrivee(self):
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                if self.tab[x][y] == 3:
                    return x,y
    
    def est_valide(self, i, j):
        return 0 <= i < self.nb_ligne() and 0 <= j < self.nb_colone()
    
    def nb_case_vide(self):
        i = 0
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                
        
    
                
    
                
            
            
## fonction principal
def main():
    tab = [[2,0,1,1,0,0,0,0,0,1],
           [1,0,1,1,0,1,1,0,1,0],
           [1,0,0,0,0,1,1,0,1,0],
           [1,0,1,1,0,1,1,0,1,0],
           [1,0,0,0,0,1,1,0,1,0],
           [1,0,1,1,1,1,1,0,1,0],
           [1,0,1,0,0,0,0,0,1,0],
           [1,0,1,0,1,1,1,1,1,0],
           [1,0,1,0,0,0,0,0,0,0],
           [1,0,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,3]]
    lab = labyrinthe(tab)
    print(lab.afficher())


## programme principal
if __name__ == '__main__':
    main()