## Importation des modules

## Déclaration des fonctions
def cercle(x):
    return 2 * 3.141592653589793 * x

def carre(x):
    return 4 * x

def triangle_equilateral(x):
    return 3 * x

def rectangle(x):
    return 2* x[0] + 2 * x[1]

def perimetre(forme, x):
    return forme(x)

def critere(x,y):
    return x >= y

def tri_insertion(tableau):
     '''
         Trie un tableau de n valeurs entières aléatoires selon la méthode du tri par insertion.
         @param entrée : tableau, liste de n entiers
         @param sortie : tableau, liste de n entiers
     '''
     for i in range(1, len(tableau)):
         element_a_placer = tableau[i]
         j = i
         while j > 0 and critere(tableau[j - 1],element_a_placer):
             tableau[j] = tableau[j - 1]
             j = j - 1
         tableau[j] = element_a_placer

     return tableau


## Programme principal



## Déclaration des classes

## fonction principale
def main():
    tableau = [7, 2, 20, 15]
    tableau_trie = tri_insertion(tableau)
    print(tableau_trie)

## Programme principal

if __name__ == '__main__':
    main()
