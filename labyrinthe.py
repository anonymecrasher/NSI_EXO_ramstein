## importation des module

## declaration des fonction

## declaration de class
class Labyrinthe:
    def __init__(self, tab):
        self.tab = tab
        
    def afficher(self):
        return self.tab
        
    @property
    def nb_ligne(self):
        return len(self.tab)
        
    @property
    def nb_colone(self):
        return len(self.tab[0])
    
    def depart(self):
        for x in range(self.nb_ligne):
            for y in range(self.nb_colone):
                if self.tab[x][y] == 2:
                    return x,y
                
    def arrivee(self):
        for x in range(self.nb_ligne):
            for y in range(self.nb_colone):
                if self.tab[x][y] == 3:
                    return x,y
    
    def est_valide(self, i, j):
        return 0 <= i < self.nb_ligne() and 0 <= j < self.nb_colone()
    
    def nb_case_vide(self):
        i = 0
        for x in range(self.nb_ligne):
            for y in range(self.nb_colone):
                if self.tab[x][y] == 0:
                    i+=1
        return i
                    
                
    def est_visite(self,i,j):
        self.tab[i,j] = 4
    def casse_fausse(self,i,j):
        self.tab[i,j] = 5
        
    def liste_voisines_libre(self,i,j):
        l = []
        if self.est_valide(i,j) and not self.tab[i-1][j] in 1,4,5:
            l.append((i,j))
        elif self.est_valide(i,j) and not self.tab[i][j-1] in 1,4,5:
            l.append((i,j))
        elif self.est_valide(i,j) and not self.tab[i+1][j] in 1,4,5:
            l.append((i,j))
        elif self.est_valide(i,j) and not self.tab[i][j+1] in 1,4,5:
            l.append((i,j))
        return l
        
    
                
                
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
    lab = Labyrinthe(tab)
    a = lab.afficher()
    print(a)


## programme principal
if __name__ == '__main__':
    main()
