## importation des modules

## Déclaration des fonction
def plus_petit(tableau):
    mini = 0
    for i in range(len(tableau)):
        if tableau[i] < tableau[mini]:
            mini = i
    return mini


def tri_selection(tableau):
    tpt = tableau
    tt = []
    for i in range(len(tableau)):
        pp = plus_petit(tpt)
        tt.append(tpt[pp])
        tpt = tpt[:pp] + tpt[pp+1:]
    return tt

def tpins(tableau):
    n = len(tableau)

    for i in range(1, n):
        element_a_inserer = tableau[i]
        j = i

        while j > 0 and tableau[j - 1] > element_a_inserer:
            tableau[j] = tableau[j - 1]
            j -= 1

        tableau[j] = element_a_inserer

    return tableau
        
        
        
        
def main():
    print(tri_selection([16, 234, 129, 195, 168, 101, 143, 214, 25, 90, 56, 133, 178, 217, 219, 96, 81, 163, 73, 220, 107, 12, 253, 71, 126, 237, 255, 224, 23, 27, 30, 215, 51, 20, 164]))
    print(plus_petit([16, 234, 129, 195, 168, 101, 143, 214, 25, 90, 56, 133, 178, 217, 219, 96, 81, 163, 73, 220, 107, 12, 253, 71, 126, 237, 255, 224, 23, 27, 30, 215, 51, 20, 164]))
    
    
## Programme principal


if __name__ == '__main__':
    main()
