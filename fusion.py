## Importation des modules

## declaration des consante

## Déclaration des fonctions
def fusion_listes(liste_1, liste_2):#liste trie
    liste_r = []
    list_1 = liste_1.copy()
    list_2 = liste_2.copy()
    while len(list_1) != 0 or len(list_2) != 0:
        a = min(list_1[0],list_2[0])
        if a == list_1[0]:
            list_1.pop(0)
        else:
            list_2.pop(0)
        liste_r.append(a)
    return list_r

    

## Déclaration des classes

## fonction principale
def main():
    pass

## programme principale
if __name__ == '__main__':
    main()
