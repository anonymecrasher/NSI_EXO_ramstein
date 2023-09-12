## importation des modules

import parcours_sequentiel
import time


## Déclaration des fonction

def main():
    
    print(dir(parcours_sequentiel))
    print(help(parcours_sequentiel))
    t = parcours_sequentiel.table_generator(1000)
    print(t)
    somme = parcours_sequentiel.somme_tableau(t)
    print("la somme est de ", somme)
    moyenne = parcours_sequentiel.average_table(t)
    print("la moyenne est de", moyenne)
    valeur_extrem = parcours_sequentiel.valeur_extreme(t)
    print("les valeur extreme sont", valeur_extrem)
    t1 = time.perf_counter()
    print(parcours_sequentiel.insere_element(t, 500, 300))
    t2 = time.perf_counter()
    print(t2- t1)
    
    
    
## Programme principal
if __name__ == '__main__':
    main()
