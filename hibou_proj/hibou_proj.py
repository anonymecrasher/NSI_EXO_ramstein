## Importation des modules
from binarytree import Node
import pikle

## Déclaration des fonctions
def sauvegarde(arbre, nom_fichier):
    fichier = open(nom_fichier + '.obj', 'wb')
    pikle.dumb(arbre,fichier)
    fichier.close()
    
def charge(nom_fichier):
    fichier = open(nom_fichier + '.obj', 'rb')
    arbre = pikle.load(fichier)
    fichier.close()
    return arbre

def q_hibou(start=True):
    if start:
        a = input('Voulez vous commencer avec un fichier contenant des donnés ?')
        if a == 'o':
            arbre = charge(str(input('entrez le nom du dossier')))
        elif a == 'n':
            ani,carac  = Node(input('''Donne moi un animal''')),
            Node(input('''Donne moi une caracteristique de l'animal'''))
            
            
    

## Déclaration des classes


## fonction principale
def main():
    arbre = Node()
    sauvegarde(arbre, 'hbarbre')
    arbre = charge('hbarbre')
    

## Programme principal
if __name__ == '__main__':
    main()