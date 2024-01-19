## Importation des modules
from binarytree import Node
import abre_binaire
import module_file

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
def parcours_infixd(arbre):
    if arbre != None:
        return parcours_infixd(arbre.right), arbre.value, parcours_infixd(arbre.left)

def is_abr(arbre):
    abr = True
    a = parcours_infixd(arbre)
    for i in range(1,len(arbre)):
        if abr:
            if arbre[i-1] >= arbre[i]:
                abr = False
    return abr
    
def parcours_postfix(arbre):
    if arbre != None:
        parcours_postfix(arbre.left)
        parcours_postfix(arbre.right)
    
        print(arbre.value)
        
def parcours_largeur(arbre):
    
    l = []
    file = module_file.File()
    file.enfiler(arbre)
    while not file.est_vide():
        temp = file.defiler()
        if temp != None:
            l.append(temp.value)

            file.enfiler(temp.left)
            file.enfiler(temp.right)
    return l

def recherche_ABR(arbre, etiquette):
    if arbre == None:
        return False
    elif arbre.value == etiquette:
        return True
    elif arbre.value < etiquette:
        return recherche_ABR(arbre.right, etiquette)
    else:
        return recherche_ABR(arbre.left, etiquette)

def min_ABR(arbre):
    if arbre.left == None:
        return arbre.value
    else:
        return min_ABR(arbre.left)
        
def max_ABR(arbre):
    if arbre.right == None:
        return arbre.value
    else:
        return max_ABR(arbre.right)
    
def inserer_ABR(arbre, etiquette):
    if arbre == None:
        return Node(etiquette)
    elif etiquette < arbre.value:
        return Node(arbre.value, inserer_ABR(arbre.left, etiquette), arbre.right)
    elif etiquette > arbre.value:
        return Node(arbre.value, arbre.left, inserer_ABR(arbre.right, etiquette))
    return arbre
    


## Déclaration des classes


## fonction principale
def main():
    arbre = abre_binaire.rand_abr(3)
    arbre5 = Node(12, Node(1, Node(6, Node(3, None, None), Node(8, None, None)), Node(0, None, None)), Node(13, Node(2, Node(13, Node(16, Node(1684, None, None), None), None), Node(11, None, None)), Node(7, None, None)))
    arbre6 = Node(50, Node(25, Node(12, Node(6), Node(15)), Node(37, Node(31), Node(43))),Node(75, Node(62,Node(56),Node(65)),Node(87,Node(81),Node(93))))
    print(arbre)
    print(est_vide(arbre))
    print(taille_arbre(arbre))
    print(hauteur_arbre(arbre))
    print(arbre5)
    print(profondeur(arbre5, 1684))
    parcours_prefix(arbre)
    parcours_infix(arbre)
    parcours_postfix(arbre)
    print(arbre5)
    
    #print(parcours_largeur(arbre6))
    arbre6 = Node(50, Node(25, Node(12, Node(6), Node(15)), Node(37, Node(31), Node(43))),Node(75, Node(62,Node(56),Node(65)),Node(87,Node(81),Node(93))))
    
    print(arbre6)
    print(recherche_ABR(arbre6,4639))
    #print(parcours_infixd(arbre6))
    #print(is_abr(arbre6))
    print(max_ABR(arbre6))
    print(inserer_ABR(arbre6,26))
    
    arbre = None
    i = 0
    while i == 10:
        arbre = inserer_ABR(arbre, i)
        i += 1
    print(arbre)
    
    

## Programme principal
if __name__ == '__main__':
    main()
