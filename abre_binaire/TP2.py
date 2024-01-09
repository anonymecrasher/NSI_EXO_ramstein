## Importation des modules
from binarytree import Node
import abre_binaire

## Déclaration des fonctions
def est_vide(arbre):
    return arbre == None

def est_une_feuille(noeud):
    return arbre.right == None and arbre.left == None

def taille_arbre(arbre):
    if est_vide(arbre):
        return 0
    else:
        return 1 + taille_arbre(arbre.left) + taille_arbre(arbre.right)
    
def hauteur_arbre(arbre):
    if est_vide(arbre):
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.left), hauteur_arbre(arbre.right))
    
def profondeur_arbre(arbre,etiquette):
    if arbre.value == etiquette:
        return 1
    pass
    
    

## Déclaration des classes


## fonction principale
def main():
    print(est_vide(abre_binaire.rand_abr(3)))
    print(taille_arbre(abre_binaire.rand_abr(3)))
    print(hauteur_arbre(abre_binaire.rand_abr(5)))

## Programme principal
if __name__ == '__main__':
    main()