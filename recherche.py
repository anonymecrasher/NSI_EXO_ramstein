def rech_dich(liste, el):
    n = len(liste)
    deb = 0
    fin = n - 1
    pos = None
    trouve = False
    while trouve == False and deb <= fin:
        mid = (deb + fin) // 2
        if liste[mid] < el:
            fin = mid + 1
        elif liste[mid] > el:
            deb = mid - 1
        elif liste[mid] == el:
            trouve = True
            pos = mid
    return pos
            
    
