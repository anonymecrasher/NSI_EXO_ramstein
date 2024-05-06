## imporatation des module

## declaration des fonction
def ouvrir_fichier(nom_de_fichier):
    with open(nom_de_fichier, 'r',encoding='utf-8') as file:
        texte = file.read()
        file.close()
    return texte
    
def recherche_force_brute(texte,motif):
    taille = len(motif)
    for carac in range(len(texte)-taille+1):
        c_test = ''
        for i in range(taille):
            c_test += texte[carac + i]
        if c_test == motif:
            return carac
        

## declaration des classe

## fonction principal
def main():
    texte = ouvrir_fichier('text.txt')
    print(texte)
    if 'AGGCTA' in texte:
        print(True)
    print(recherche_force_brute(texte,'AE'))

## programme principal
if __name__ == '__main__':
    main()