## imporatation des module

## declaration des fonction
def ouvrir_fichier(nom_de_fichier):
    with open(nom_de_fichier, 'r',encoding='utf-8') as file:
        texte = file.read()
        file.close()
    return texte

def table_de_saut(motif):
    tab = {}
    for i in range(len(motif)):
        tab[motif[i]] = None
    for i in range(len(motif)):
        if tab[motif[i]] == None:
            tab[motif[i]] = len(motif) - i -1
    return tab


## declaration des classe

## fonction principal
def main():
    texte = ouvrir_fichier('text.txt')
    print(texte)
    if 'AGGCTA' in texte:
        print(True)
        
    print(table_de_saut('AGGCTA'))

## programme principal
if __name__ == '__main__':
    main()