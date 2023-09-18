## importation des modules

## Déclaration des fonction
def rech_dich(liste, el):
    liste.sort()
    n = len(liste)
    deb = 0
    fin = n - 1
    pos = None
    trouve = False
    while trouve == False and deb <= fin:
        mid = (deb + fin) // 2
        if liste[mid] < el:
            deb = mid + 1
        elif liste[mid] > el:
            fin = mid - 1
        elif liste[mid] == el:
            trouve = True
            pos = mid
    return pos






def main():
    t = [9,8,6,7,6,3,1,2,6,45,2,4]
    print(rech_dich(t, 5))

## Programme principal
if __name__ == '__main__':
    main()
    
