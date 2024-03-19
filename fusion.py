## Importation des modules
import random


## declaration des consante

## Déclaration des fonctions
def fusion_listes(liste_1, liste_2):#liste trie
    liste_r = []
    
    while len(liste_1) != 0 and len(liste_2) != 0:
        if liste_1[0] < liste_2[0]:
            liste_r.append(liste_1[0])
            liste_1.pop(0)
        else:
            liste_r.append(liste_2[0])
            liste_2.pop(0)
        
    return liste_r + liste_1 + liste_2

def fusion_listes_r(liste_1,liste_2):
    if liste_2 == []:
        return liste_1
    elif liste_1 == []:
        return liste_2
    else:
        if liste_1[0] < liste_2[0]:
            return [liste_1[0]] + fusion_listes_r(liste_1[1:],liste_2)
        else:
            return [liste_2[0]] + fusion_listes_r(liste_2[1:],liste_1)

def tri_fusion(liste):
    if len(liste) == 1:
        return liste
    else:
        mi = len(liste) // 2
        return fusion_listes_r(tri_fusion(liste[:mi]), tri_fusion(liste[mi:]))
    

    

## Déclaration des classes


## fonction principale
def main():
    liste = [random.randint(0,1000) for i in range(10)]
    
    print(liste)
    print(tri_fusion(liste))
## programme principale
if __name__ == '__main__':
    main()
