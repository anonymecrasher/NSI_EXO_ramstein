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

def critere_dec(x,y):
    return x <= y
def critere_nom(x,y):
    return x[0] >= y[0]
def critere_prenom(x,y):
    return x[1] >= y[1]
def critere_age(x,y):
    return x[2] > y[2]

def derive(f,x):
    h = 1 * 10 ** -11
    return (f(x+h) -f(x))/h

def carre(x):
    return x ** 2



def tri_insertion(tableau,critere):
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

def f(x):
    return x * 5

def g(x):
    return x ** 2
def is_in10and20(x):
    return x>10 and x<20
## Programme principal



## Déclaration des classes

## fonction principale
def main():
    add_one = lambda x: x+1
    def divise(f1,f2):
        return lambda x: f1(x) / f2(x)
    f = lambda x: x * 5
    g = lambda x: x ** 2
    h = divise(f,g)
    cercle = lambda x: 2 * x[0] * 3.141592653589793
    carre = lambda x: 4 * x[0]
    triangle_equilateral = lambda x: 3 * x[0]
    rectangle = lambda x: (x[0] + x[1])*2
    perimetre = lambda f,x: f(x)
    
    tableau = [7, 2, 20, 15]
    list_triplet = [('Rakotovao', 'Ny-Harena',  2006),('Farvacque', 'Mathias', 2006),('morenvillé','martin',2006),('Douchet','lilian',2006),('lemoine','yanko',2006)]
    tableau_trie = tri_insertion(list_triplet,critere_age)
    for i in range(1,100):
        print("h'("+str(i)+ ')=',derive(h,i))
        print('h('+str(i)+ ')=',h(i))
    print(tableau_trie)
    print(add_one(2))

## Programme principal

if __name__ == '__main__':
    main()#c'est le bordel se programme
