#importation de module
import timeit
import matplotlib.pyplot as plt# sa aurait été un plus cool si vous aviez precisez le module a utiliser en detaille

#Création du lexique:

with open('lexique.txt', 'r', encoding='utf8') as f:
    mots = f.readlines()

LEXIQUE = [m.lower().rstrip('\n') for m in mots]

#declaration des constante

equivalence = {'à':'a' , 'â':'a' , 'ä':'a' , 'é':'e' , 'è':'e' , 'ê':'e' , 'ë':'e' , 'î':'i' ,
               'ï':'i' , 'ô':'o' , 'ö':'o' , 'ù':'u' , 'û':'u' , 'ü':'u' , 'ÿ':'y' , 'ç':'c'}

#Définition des fonctions

def sans_accent(mot:str)->str:
    '''
    @input : mot  ; type = str
    @output: motr ; type = str
    will return the word with out accent
    '''
    mot = str(mot)
    motr = ''
    for i in mot:
        if i in  'abcdefghijklmnopqrstuvwxyz':
            motr += i
        elif i in """-.'""":
            pass
        else:
            motr += equivalence[i]
    return motr

def clef_mot(chaine:str)->str:
    """
    cette methode transforme la chaine de caractere passée en paramettre en liste
    Elle trie en utillisant la methode sort des list en python.
    pour chaque caractere de la liste :
    elle ajoute le caractere dans une chaine de caractere qui sera renvoyée.
    """
    
    s = ""
    l = list(sans_accent(chaine))
    l.sort()
    for carac in l:
        s += carac
    return s

def anagramme_via_clef(mot1:str,mot2:str)->bool:
    """
    @input  : mot1  ; type = str
    @input  : mot2  ; type = str
    @output type = bool
    this will test if the key of the two words is the same
    """
    clef_mot1 = clef_mot(mot1)
    clef_mot2 = clef_mot(mot2)
    return clef_mot1 == clef_mot2

def mesure_anagramme_clef(nb_mots):
    '''
    Réalise la mesure du temps necessaire pour trouver
    les anagrammes de i mots sur un lexique d'une taille i.
    
    La méthode employée correspond a la creation d'une clef
    et a la recherche des clef des autre mots auquel on le compare.
    
    La complexité dépend de la taille du lexique
    '''
    tab_mesures = []
    
    for i in range(0,nb_mots):
        
        #temps du debut
        temps_debut = timeit.default_timer()
        for mot in LEXIQUE[:i]:
            for mot_du_lexique in LEXIQUE[:i]:
                anagramme_via_clef(mot, mot_du_lexique)
            
        #temps de fin
        temps_fin = timeit.default_timer()
        # ajout de la durée dans le tableau la case i correspond a la
        # recherche des anagramme de i mot sur un lexique de i mots
        tab_mesures.append(temps_fin-temps_debut)
    print(str(sum(tab_mesures)) + 'secondes')
    
    # Creation d'un graphique: l'absice corespond a un nombre de mots
    # et l'ordonné correspond au temps neccessaire
    plt.plot([i for i in range(nb_mots)],tab_mesures)
    # Creation d'un fichier png correspondant a la courbe créée grace a la methode plot
    plt.savefig('fig_clef.png')
    plt.clf()
    
def dictionnaire_du_lexique(lexique:list)->dict:
    """
    @input  : lexique  ; type = str
    @output : dico     ; type = dict
    returns a dictionary containing all the keys of the lexique values
    """
    dico = {}
    for i in lexique:
        dico[str(i)] = clef_mot(i)
    return dico
        
def anagramme_via_dictionnaire(mot:str,dictio:dict)->list:
    #clef_du_mot = clef_mot(mot)
    
    #s = []
    #for i in dictio:
    #    if dictio[str(i)] == clef_du_mot:
    #       s.append(str(i))
    #return s
    clef_du_mot = clef_mot(mot)
    
    # Utilisation directe du dictionnaire fourni en paramètre
    return [i for i in dictio if dictio[i] == clef_du_mot]

def mesure_anagramme_dico(nb_mots):
    '''
    Réalise la mesure du temps necessaire pour trouver
    les anagrammes de i mots sur un lexique d'une taille i.
    
    La méthode employée correspond a la creation d'une clef
    et a la recherche des clef des autre mots auquel on le compare.
    
    La complexité dépend de la taille du lexique
    '''
    """
    tab_mesures = []
    
    for i in range(0,nb_mots):
        lexique_dict = dictionnaire_du_lexique(LEXIQUE[:i])
        #temps du debut
        temps_debut = timeit.default_timer()
        
        for mot in LEXIQUE[:i]:
            anagramme_via_dictionnaire(mot,lexique_dict)
            
        #temps de fin
        temps_fin = timeit.default_timer()
        # ajout de la durée dans le tableau la case i correspond a la
        # recherche des anagramme de i mot sur un lexique de i mots
        tab_mesures.append(temps_fin-temps_debut)
    print(str(sum(tab_mesures)) + 'secondes')
    
    # Creation d'un graphique: l'absice corespond a un nombre de mots
    # et l'ordonné correspond au temps neccessaire
    plt.plot([i for i in range(nb_mots)],tab_mesures)
    # Creation d'un fichier png correspondant a la courbe créée grace a la methode plot
    plt.savefig('fig_dico.png')
    plt.clf()
    """
    tab_mesures = []
    
    # Création du dictionnaire une seule fois à l'extérieur de la boucle
    lexique_dict = dictionnaire_du_lexique(LEXIQUE[:nb_mots])
    
    for i in range(0, nb_mots):
        # Temps du début
        temps_debut = timeit.default_timer()
        
        for mot in LEXIQUE[:i]:
            anagrammes = anagramme_via_dictionnaire(mot, lexique_dict)
            # Utilisez les anagrammes si nécessaire
            # print(f"Anagrammes de '{mot}': {anagrammes}")
            
        # Temps de fin
        temps_fin = timeit.default_timer()
        
        # Ajout de la durée dans le tableau
        # La case i correspond à la recherche des anagrammes de i mots sur un lexique de i mots
        tab_mesures.append(temps_fin - temps_debut)
    
    print(str(sum(tab_mesures)) + ' secondes')
    
    # Création d'un graphique : l'abscisse correspond à un nombre de mots
    # et l'ordonnée correspond au temps nécessaire
    plt.plot([i for i in range(nb_mots)], tab_mesures)
    # Création d'un fichier png correspondant à la courbe créée grâce à la méthode plot
    plt.savefig('fig_dico.png')
    plt.clf()
    
#declaration des class

#fonction principal

def main():
    print(sans_accent('orangé'))
    print(clef_mot('orangé'))
    print(anagramme_via_clef('orangé','aegnar'))
    #lexique_dict = dictionnaire_du_lexique(LEXIQUE)
    #print(anagramme_via_dictionnaire('martin', lexique_dict))
    mesure_anagramme_clef(500)# la courbe semble comm celle d'un polynome donc sela corespond a une complexité quadratique 190.92437120096292secondes

    mesure_anagramme_dico(500)# la courbe semble lineaire donc sela corespond a une complexité lineaire 4 seconde
    

    
    
#Programme principal
    
if __name__ == '__main__':
    main()