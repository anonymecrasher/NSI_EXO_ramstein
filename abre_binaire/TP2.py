## Importation des modules
from binarytree import Node
import abre_binaire

## Déclaration des fonctions
def est_vide(arbre):
    return arbre == None

def est_une_feuille(noeud):
    return noeud.right == None and noeud.left == None

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
    if est_vide(arbre):
        return 0,0
    else:
        if arbre.value == etiquette:
            return 1,1
        else:
            left = profondeur_arbre(arbre.left,etiquette)
            right = profondeur_arbre(arbre.right,etiquette)
            if left[1] or right[1]:
                return (1 + min(left[0],right[0]),1)
            else:
                return (float("+INF"), 0)
# float("+INF")
        
def i_profondeur_arbre(arbre,etiquette):
    r = profondeur_arbre(arbre,etiquette)
    if r[1] == 1:
        return r[0]
    else:
        return False

def profondeur(arbre,etiquette):
    if est_vide(arbre):
        return None
    if arbre.value == etiquette:
        return 0
    else:
        left = profondeur(arbre.left,etiquette)
        right = profondeur(arbre.right,etiquette)
        if left == None and right == None:
            return None
        if left != None:
            return 1 + left
        if right != None:
            return 1 + right
        if left != None and right != None:
            return 1 + min(left,right)
def parcours_prefix(arbre):
    if arbre != None:
        print(arbre.value)
        parcours_prefix(arbre.left)
        parcours_prefix(arbre.right)
    
def parcours_infix(arbre):
    if arbre != None:
        parcours_infix(arbre.left)
        print(arbre.value)
        parcours_infix(arbre.right)
    
def parcours_postfix(arbre):
    if arbre != None:
        parcours_postfix(arbre.left)
        parcours_postfix(arbre.right)
    
        print(arbre.value)


## Déclaration des classes


## fonction principale
def main():
    arbre = abre_binaire.rand_abr(3)
    arbre5 = Node(12, Node(1, Node(6, Node(3, None, None), Node(8, None, None)), Node(0, None, None)), Node(13, Node(2, Node(13, Node(16, Node(1684, None, None), None), None), Node(11, None, None)), Node(7, None, None)))
    print(arbre)
    print(est_vide(arbre))
    print(taille_arbre(arbre))
    print(hauteur_arbre(arbre))
    print(arbre5)
    print(profondeur(arbre5, 1684))
    parcours_prefix(arbre)
    parcours_infix(arbre)
    parcours_postfix(arbre)
    
    

## Programme principal
if __name__ == '__main__':
    main()
