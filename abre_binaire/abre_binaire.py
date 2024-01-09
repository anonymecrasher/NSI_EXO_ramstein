## Importation des modules
from binarytree import Node
import random
## Déclaration des fonctions
def rand_abr(i):
    if i == 0:
        return Node(random.randint(0,1000))
    else:
        return Node(random.randint(0,1000),rand_abr(i-1),rand_abr(i-1))
    

## Déclaration des classes
class Nodee:
    def __init__(self, value=0 ,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
        

## fonction principale
def main():
    noeud_A = Node("A", None, None)
    noeud_E = Node("E", None, None)
    noeud_I = Node("I", None, None)
    noeud_K = Node("K", None, None)
    noeud_L = Node("L", None, None)
    noeud_J = Node("J", None, noeud_K)
    noeud_B = Node("B", noeud_A, None)
    noeud_D = Node("D", noeud_J, noeud_E)
    noeud_H = Node("H", noeud_L, noeud_I)
    noeud_C = Node("C", noeud_B, noeud_D)
    noeud_G = Node("G", None, noeud_H)
    noeud_F = Node("F", noeud_C, noeud_G)
    arbre1 = noeud_F
    
    arbre2 = Node('manchot')
    arbre2.left = Node('poule')
    arbre2.left.left = Node('chat')
    arbre2.left.left.left = Node('rat')
    arbre2.left.left.right = Node('chien')
    arbre2.left.right = Node('pigeon')
    arbre2.right = Node('canari')
    arbre2.right.left = Node('léopard')
    arbre2.right.right = Node('vache')
    arbre2.right.right.right = Node('gazelle')
    
    arbre3 = Node(7, Node(11, None, Node(2, None, None)), Node(1, Node(9, None, None), Node(13,None, None)))
    
    print(arbre1)
    print(arbre2)
    print(arbre3)
    
    arbre4 = Node(12)
    arbre4.left = Node(1)
    arbre4.left.left = Node(6)
    arbre4.left.right = Node(0)
    arbre4.left.left.left = Node(3)
    arbre4.left.left.right = Node(8)
    arbre4.right = Node(5)
    arbre4.right.left = Node(2)
    arbre4.right.left.right = Node(11)
    arbre4.right.right = Node(7)
    arbre4.right.right.right = Node(13)
    
    print(arbre4)
    
    arbre5 = rand_abr(4)
    print(arbre5.is_balanced)
    print(arbre5.is_complete)
    print(arbre5.is_perfect)
    print(arbre5.is_strict)

## Programme principal
if __name__ == '__main__':
    main()