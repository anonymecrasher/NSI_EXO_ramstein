#DS mathias farvacque

# importation des module

# declaration des fonction
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
    
    

# declaration des class

# fonction principal
def main():
    pass
# programme principal
if __name__ == '__main__':
    main()