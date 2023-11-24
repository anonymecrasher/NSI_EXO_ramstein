## Importation des modules


## Déclaration des classes

class Maillon:
    def __init__(self, valeur = None, suivant = None):
        self.valeur = valeur
        self.suivant = suivant


class Liste_chainee:
    def __init__(self, iterable = None):
        if iterable == None:
            self.tete = None
        else:
            self.tete = Maillon(iterable[0])
            for i in range(1, len(iterable)):
                self.ajouter_element_queue(iterable[i])
        
    def est_vide(self):
#         if self.tete == None:
#             return True
#         else:
#             return False

        return self.tete == None
    
    def ajouter_element_queue(self, valeur):
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
            liste_valeurs = []
            maillon = self.tete
            liste_valeurs.append(maillon.valeur)
            while maillon.suivant != None:
                maillon = maillon.suivant
                liste_valeurs.append(maillon.valeur)
            
            return liste_valeurs

    def longueur(self):
        if self.est_vide():
            return 0
        else:
            maillon = self.tete
            longueur = 1
            while maillon.suivant != None:
                longueur = longueur + 1
                maillon = maillon.suivant
            
            return longueur

    def extrait_element(self, position):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        assert position >= 0 and position < self.longueur(), 'index out of range'
        
        maillon = self.tete
        
#         for i in range(position):
#             maillon = maillon.suivant

        i = 0
        while i != position:
            maillon = maillon.suivant
            i = i + 1

        return maillon.valeur

    def ajouter_element_tete(self, valeur):
        self.tete = Maillon(valeur, self.tete)

    def supprimer_element_queue(self):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'

        maillon = self.tete
        
        i = 0
        position = self.longueur() - 2
        
        while i != position:
            maillon = maillon.suivant
            i = i + 1
            
        maillon.suivant = None

    def supprimer_element_tete(self):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        
        self.tete = self.tete.suivant

    def inserer_element(self, valeur, position):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        assert position >= 0 and position <= self.longueur(), 'index out of range'
        
        if position == 0:
            self.ajouter_element_tete(valeur)
        else:
            maillon = self.tete
            
            i = 0
            while i != position - 1:
                maillon = maillon.suivant
                i = i + 1
                
            maillon.suivant = Maillon(valeur, maillon.suivant)
            
    def supprimer_element(self, position):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        assert position >= 0 and position < self.longueur(), 'index out of range'
 
        if position == 0:
            self.supprimer_element_tete()
        elif position == self.longueur() - 1:
            self.supprimer_element_queue()
        else:
            maillon = self.tete
            
            i = 0
            while i != position - 1:
                maillon = maillon.suivant
                i = i + 1
                
            maillon.suivant = maillon.suivant.suivant

    def chercher_element(self, valeur):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        
        liste_positions = []
        maillon = self.tete
        if maillon.valeur == valeur:
            liste_positions.append(0)
        i = 0
        while maillon.suivant != None:
            i = i + 1
            maillon = maillon.suivant
            if maillon.valeur == valeur:
                liste_positions.append(i)
                
        return liste_positions

    def renverser(self):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'
        
        nouvelle_liste = Liste_chainee()
        
        maillon = self.tete
        nouvelle_liste.ajouter_element_tete(maillon.valeur)
        while maillon.suivant != None:
            maillon = maillon.suivant
            nouvelle_liste.ajouter_element_tete(maillon.valeur)
            
        self.tete = nouvelle_liste.tete

    def modifier_valeur(self, position, valeur):
        assert self.est_vide() == False, 'La liste ne doit pas être vide'        
        assert position >= 0 and position < self.longueur(), 'index out of range'
        
        maillon = self.tete
        
        i = 0
        while i != position:
            maillon = maillon.suivant
            i = i + 1
            
        maillon.valeur = valeur       
        
    def permuter_elements(self, position_1, position_2):
        assert self.longueur() >= 2, 'La liste doit être au moins de longueur 2'
        assert position_1 >= 0 and position_1 < self.longueur(), 'index 1 out of range'
        assert position_2 >= 0 and position_2 < self.longueur(), 'index 2 out of range'
        
        valeur_1 = self.extrait_element(position_1)
        valeur_2 = self.extrait_element(position_2)
        
        self.modifier_valeur(position_1, valeur_2)
        self.modifier_valeur(position_2, valeur_1)


## Déclaration des fonctions


## Programme principal

l1 = Liste_chainee()
print(l1.list())

l1 = Liste_chainee((4, 5, 6, 7))
print(l1.list())

l1 = Liste_chainee([4, 5, 6, 7])
print(l1.list())

l1 = Liste_chainee('abcd')
print(l1.list())
