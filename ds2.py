## importation des module

## declaration des fonction
def empaqueter(liste_masses, c):
    """
    Renvoie le nombre minimmal des boites nécessaires pour empaqueter les objets de la lites liste_masses,sachant
    que chaque boite ne peux contenir au maximum c kilogrammes
    """
    n = len(liste_masses)
    nb_boites = 0
    boites = [0 for i in range(n)]
    for masse in liste_masses:
        i = 0
        while i < nb_boites and boites[i] + masse >c:
            i += 1
        if i == nb_boites:
            nb_boites += 1
        boites[i] += masse
    return nb_boites
## declaration des classe

## fonction principal
def main():
    print(empaqueter([1,2,3,4,5], 10))
    print(empaqueter([1,2,3,4,5], 5))
    print(empaqueter([2,3,4,5,7,8,9,6], 11))
    
## programme princpal
if __name__ == '__main__':
    main()