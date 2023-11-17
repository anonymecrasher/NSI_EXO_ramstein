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
        if self.est_vide():
            self.tete = Maillon(valeur)
        else:
            maillon = self.tete
            while maillon.suivant != None:
                maillon = maillon.suivant
            maillon.suivant = Maillon(valeur)
    def list(self):
        if self.est_vide():
            return []
        else:
        
            temp= []
            maillon = self.tete
            while maillon.suivant != None:
                temp.append(maillon.valeur)
                maillon = maillon.suivant
            temp.append(maillon.valeur)
                
            return temp
    
    def len(self):
        if self.est_vide():
            return 0
        else:
            temp = 1
            maillon = self.tete
            while maillon.suivant != None:
                maillon = maillon.suivant
                temp += 1
            return temp
    
    def extract_element(self,pos=0):
        assert pos < self.len(), 'index out of range'
        assert pos >= 0, 'index out of range'
        if self.est_vide():
            return 0
        else:
            maillon = self.tete
            for i in range(pos):
                maillon = maillon.suivant
            return maillon.valeur
    
    def ajouter_element_tete(self,valeur = 0):
        self.tete = Maillon(valeur, self.tete)
    
    def supprimer_element_queue(self):
        
        maillon = self.tete
        x = 0
        long = self.len()
        while long-2>x:
            maillon = maillon.suivant
            x+=1
        maillon.suivant = None
    
    def supprimer_element_tete(self):
        self.tete = self.tete.suivant
        
    def inserer_element(self):
        pass
        
        
        
        
        
            
        
        
        

# fonction principal
def main():
    l1 = Liste_chainee()
    
    print(l1.tete)
    l1.ajouter_element_queue(5)
    print(l1.tete.valeur)
    l1.ajouter_element_queue(7)
    print(l1.list())
    print(l1.len())
    print(l1.extract_element(1))
    l1.ajouter_element_tete()
    print(l1.list())
    l1.supprimer_element_queue()
    print(l1.list())
    

# programme principal
if __name__ == '__main__':
    main()
