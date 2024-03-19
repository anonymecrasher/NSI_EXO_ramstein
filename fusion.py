## Importation des modules
import random
import time

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

def recherche_lineaire(tableau,el):
    for i in range(len(tableau)):
        if tableau[i] == el:
            return i
    return None


"""la recherche dichotomique est un algorithme pour savoir
si un nombre est contenu dans une liste (trié) pour il compare la valeur a la mediane de la liste
est refait la ensuite la dichotomie sur la liste + petite qui va de 0 a mediane si valeur<mediane
ou mediane a fin si valeur > mediane
"""
def dichotomie(tab,x):
    """
    tab : tableau trie dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # Cas 1
    if len(tab) == 0:
        return False,1
    # Cas 2
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    # Cas 3
    debut = 0
    fin = len(tab)-1
    while debut <= fin:
        m = (debut + fin )// 2
        if x == tab[m]:
            return True
        elif x > tab[m]:
            debut = m + 1
            
        else:
            fin = m - 1
# corresspond a la situation ou x n'est pas dans la liste
    return False, 3

def recur_dichotomie(tab, x):
    """
    tab : tableau trie dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    if len(tab) == 0:
        return False,1
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    
    m =  (len(tab)-1) // 2
    if x == tab[m-1]:
        return True
    elif  x > tab[m]:
        return recur_dichotomie(tab[m + 1:],x)
    else:
        return recur_dichotomie(tab[:m - 1],x)
    
    return False
    
    

## Déclaration des classes


## fonction principale
def main():
    liste = [random.randint(0,100) for i in range(975)]
    
    print(liste)
    print(tri_fusion(liste))
    liste_t = tri_fusion(liste)
    a = random.randint(0,100)
    print(a)
    t0 = time.perf_counter_ns()
    recherche_lineaire(liste_t, a)
    t1 = time.perf_counter_ns()
    print(t1 - t0)
    t0 = time.perf_counter_ns()
    dichotomie(liste_t, a)
    t1 = time.perf_counter_ns()
    print(t1 - t0)
    t0 = time.perf_counter_ns()
    recur_dichotomie(liste_t, a)
    t1 = time.perf_counter_ns()
    print(t1 - t0)
    
    
## programme principale
if __name__ == '__main__':
    main()
