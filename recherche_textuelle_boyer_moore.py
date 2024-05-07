## imporatation des module

## declaration des fonction
def ouvrir_fichier(nom_de_fichier):
    with open(nom_de_fichier, 'r',encoding='utf-8') as file:
        texte = file.read()
        file.close()
    return texte

def table_de_saut(motif):
    tab = {}
    for i in range(len(motif)-1):
        tab[motif[i]] = len(motif) - i -1
    tab['autre'] = len(motif)
    return tab

def dictance(table,caractere):
    return table[caractere]

def distance2(table,caractere,nb_caractere):
    if caractere in table:
        if table[caractere] - nb_caractere > 0:
            return table[caractere] - nb_caractere
        else:
            return table['autre'] - nb_caractere
    else:
        return table['autre']
    
def compare_texte_motif(texte, motif, position):
    i = len(motif)
    flag = True
    while i > 0 and flag:
        flag = texte[position+i-1] == motif[i-1]
        i -= 1
    if not flag:
        return i
    return None
    
def recherche_boyer_moore(texte, motif):
    tab = table_de_saut(motif)
    i = 0
    while i + len(motif) < len(texte):
        print(i)
        result_temp = compare_texte_motif(texte, motif, i)
        if result_temp == None:
            return i
        else:
            dis = distance2(tab,motif[result_temp],len(motif) - result_temp)
            print()
            print(dis)
            print()
            i += dis
    return None
        

## declaration des classe

## fonction principal
def main():
    texte = ouvrir_fichier('text.txt')
    print(texte)
    if 'AGGCTA' in texte:
        print(True)
        
    print(table_de_saut('AGGCTA'))
    print(compare_texte_motif(texte,'AGGCTA',1))
    print()
    print(recherche_boyer_moore(texte, 'AGGCTA'))

## programme principal
if __name__ == '__main__':
    main()
