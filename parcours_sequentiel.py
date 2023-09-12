## importation des modules
import random

## Déclaration des fonction
def table_generator():
    t = []
    for i in range(random.randint(3, 18)):
        t.append(random.randint(0, 256))
    return t

def somme_tableau(t):
    ans = 0
    for i in t:
        ans += int(i)
    return ans

def average_table(t):
    """
    doc ...
    """
    ans = somme_tableau(t)
    ans = ans /len(t)
    return ans

def valeur_extreme(t):
    
    mini = t[0]
    maxx = t[0]
    for i in t:
        if i < mini:
            mini = i
        if i > maxx:
            maxx = i
    return mini, maxx
    
def insere_element(t, p, e):
    t = t[:p] + [e] + t[p:]
    return t



def main():
    
    help(average_table)
    
    t = table_generator()
    t = [random.randint(0,256) for i in range(random.randint(3,18))]
    print(t)
    print(average_table(t))
    print(insere_element(t, 1, 97))



## Programme principal


if __name__ == '__main__':
    main()
