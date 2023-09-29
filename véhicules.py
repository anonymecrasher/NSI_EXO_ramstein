## importation des modules

## Déclaration des classes
class Voiture():
    
    def __init__(self,
                 moteur = 'essence',
                 couleur = 'bleu',
                 puissance = '130',
                 nb_porte = '4',
                 boite_vitesse = 'manuelle',
                 masse = '1000',
                 masse_vide = '1000',
                 masse_PTAC = '1300'):
        self.moteur = moteur
        self.couleur = couleur
        self.puissance = puissance
        self.nb_porte = nb_porte
        self.boite_vitesse = boite_vitesse
        self.masse = masse
        self.masse_vide = masse_vide
        self.masse_PTAC = masse_PTAC
        
    def __caracteristique(self):
        return {'moteur': self.moteur,
                'couleur': self.couleur,
                'puissance': self.puissance,
                'nombre de porte': self.nb_porte,
                'boite_vitesse': self.boite_vitesse,
                'masse': self.masse,
                'masse_vide': self.masse_vide,
                'masse_PTAC': self.masse_PTAC}
    
    def affiche_caracteristique(self):
        dico = self.__caracteristique()
        print('Les caracteristique du véhicule sont:')
        for cle, valeur  in dico.items():
            print(cle, ':', valeur)
    
    
    def modifie_couleur(self, nouvelle_couleur):
        self.couleur = nouvelle_couleur
    
    def modifie_moteur(self, new_moteur):
        self.moteur = new_moteur
    
    def modifie_puissance(self, new_puissance):
        self.puissance = new_puissance
        
    
    def charge(self, add_masse):
        self.masse = str(int(self.masse) + int(add_masse))
        if self.masse < self.masse_PTAC:
            return True
        else:
            return False
    def decharge(self, add_masse):
        self.masse = str(int(self.masse) - int(add_masse))
        if self.masse < self.masse_PTAC:
            return True
        else:
            return False
    


## Déclaration des fonction





def main():
    voiture_1 = Voiture()
    voiture_2 = Voiture('diesel', 'orange', '240')
    voiture_3 = Voiture(puissance='90')
    voiture_1.modifie_couleur('blouge')

    voiture_2.affiche_caracteristique()
    help(Voiture)


## Programme principal
if __name__ == '__main__':
    main()
