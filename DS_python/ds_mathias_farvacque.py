#DS mathias farvacque

# importation des module

# declaration des fonction

# declaration des class
class TipTop():
    def __init__(self, users=[]):
        self.users = users
    def max_like(self):
        '''
        @param_entre : self
        @param_sortie : noms
        
        renvoie le noms de l'utilisateur ayant obtenus le plus de like
        '''
        maxi = self.users[0].nb_like
        noms = self.users[0].nom
        for i in self.users:
            if i.nb_like > maxi:
                maxi = i.nb_like
                noms = i.nom
        return noms
            
        
class Utilisateur():
    def __init__(self, nom, nb_like,publications):
        self.nom = nom
        self.nb_like = nb_like
        self.publications = publications
    def afficher_information(self):
        '''
        @param_entre : self
        
        affiche les attribut de l'utilisateur
        '''
        print(self.nom,'a',self.nb_like,'like sur',self.publications,'publications')

# fonction principal
def main():
    # on instancie 3 utilisateur
    user1 = Utilisateur('ny',59,4)
    user2 = Utilisateur('mathias',1,3)
    user3 = Utilisateur('martin',9,1)
    
    # on instancie le reseau
    reseau_TipTop = TipTop([user1,user2,user3])
    
    #1er teste de la fonction max_like()
    a = reseau_TipTop.max_like()
    print(a)
    
    #2e teste de la fonction max_like()
    user3.nb_like = 999
    a = reseau_TipTop.max_like()
    print(a)
    
    # test de la fonction affiche information
    user3.afficher_information()
    

# programme principal
if __name__ == '__main__':
    main()