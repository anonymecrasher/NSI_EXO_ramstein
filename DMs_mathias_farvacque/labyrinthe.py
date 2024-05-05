## importation des module

## declaration des fonction

## declaration de class
class Labyrinthe:
    def __init__(self, tab):
        self.tab = tab
        
    def afficher(self):# fonction qui affiche le labyrinthe
        for i in self.tab:
            print(i)
    
    def __str__(self):# fonction permettant de modifier le comportement d'un print sur l'objet labyrinthe 
        ret = ""
        for i in self.tab:
            ret += str(str(i) + "\n")
        return ret
            
    def nb_ligne(self):# renvoie le nombre de ligne
        return len(self.tab)
        
    def nb_colone(self):# renvoie le nombre de colone
        return len(self.tab[0])
    
    def depart(self):# renvoie les coordonne x et y du depart
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                if self.tab[x][y] == 2:
                    return x,y
                
    def arrivee(self):# renvoie les coordonne x et y de l'arrivé
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                if self.tab[x][y] == 3:
                    return x,y
    
    def est_valide(self, i, j): # renvoie True si la case est dans le labyrinthe
        return 0 <= i < self.nb_ligne() and 0 <= j < self.nb_colone()
    
    def nb_case_vide(self): # renvoie le nombre de case libre
        i = 0
        for x in range(self.nb_ligne()):
            for y in range(self.nb_colone()):
                value_in_xy = self.tab[x][y]
                if value_in_xy == 0 or value_in_xy == 2 or value_in_xy == 3:
                    i += 1
        return i
                    
                
    def est_visite(self,i,j): # set une case en tant que case deja visité 
        print(i,j)
        self.tab[i][j] = 4
        
    def casse_fausse(self,i,j): # set une case en tant que case fausse 
        self.tab[i][j] = 5
        
    def liste_voisines_libre(self,i,j): # fonction renvoyant une liste des case voisine libre d'une case ayant pour coordonne i et j
        l = []
        if self.est_valide(i-1,j) and not (self.tab[i-1][j] in (1,4,5)):
            l.append((i-1,j))
        
        if self.est_valide(i,j-1) and not (self.tab[i][j-1] in (1,4,5)):
            l.append((i,j-1))
        if self.est_valide(i+1,j) and not (self.tab[i+1][j] in (1,4,5)):
            l.append((i+1,j))
            
        if self.est_valide(i,j+1) and not (self.tab[i][j+1] in (1,4,5)):
            l.append((i,j+1))
            
        return l
    
    def test_co_is_value(self,co,value): # fonction qui teste si la valeur a certaine coordonné co (type tuple ou liste contenant 2 entier )est egale a value
        if self.est_valide(co[0], co[1]):
            return self.tab[co[0]][co[1]] == value
                
    
    def explore(self): # fonction renvoyant le chemin du depart a l'arriver
        """
        petit probleme ne renvoie pas forcement le chemin le plus court si il existe plusieur chemin(il en renverra un seul parmi les chemin existant)
        """
        dep = self.depart()
        curent_pos = dep
        pile = [dep]
        arr = self.arrivee()
        while curent_pos != arr and len(pile) != 0:
            print(self)
            if not self.test_co_is_value((curent_pos),1):
                i = int(curent_pos[0])
                j = int(curent_pos[1])
                voisin = self.liste_voisines_libre(i,j)
                if len(voisin) == 0:
                    if not self.test_co_is_value((curent_pos),0):
                        self.casse_fausse(curent_pos[0],curent_pos[1])
                        pile.pop()
                        curent_pos = pile[-1]
                    else:
                        self.casse_fausse(curent_pos[0],curent_pos[1])
                        curent_pos = pile[-1]
                else:
                    self.est_visite(i,j)
                    pile.append(curent_pos)
                    curent_pos = voisin[0]
        pile.pop(0)
        return pile
                    
                
            
        
        
    
                
                
## fonction principal
def main():
    tab = [[2,0,1,1,0,0,0,0,0,1],# (pas le meme labyrinthe que dans le sujet
           [1,0,1,1,0,1,1,0,1,0],
           [1,0,0,0,0,1,1,0,1,0],
           [1,0,1,1,0,1,1,0,1,0],
           [1,0,0,0,3,1,1,0,1,0],
           [1,0,1,1,1,1,1,0,1,0],
           [1,0,1,0,0,0,0,0,1,0],
           [1,0,1,0,1,1,1,1,1,0],
           [1,0,1,0,0,0,0,0,0,0],
           [1,0,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0]]
    lab = Labyrinthe(tab)
    lab.afficher()
    print()
    #print(lab)
    #(lab.est_valide(-5, 15))
    #print(lab.est_valide(4, 15))
    #print(lab.est_valide(4, 4))
    #print(lab.est_valide(-5, 4))
    #print(lab.nb_case_vide())
    #print(lab.liste_voisines_libre(0,1))
    print(lab.explore())
    print(lab)
    
    


## programme principal
if __name__ == '__main__':
    main()