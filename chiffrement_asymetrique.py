## importation des module
import random


## declaratition des fonction
def generer_cle(n):
    cle = ''
    for i in range(n):
        cle += chr(random.randint(33 , 126))
        #cle = cle +
    return cle

def generer_ensemble_cles(n, p):
    dico_cle = {}
    for i in range(n):
        al = random.randint(0,99999)
        while al in dico_cle:
            al = random.randint(0,99999)
        dico_cle[al] = (generer_cle(p))
        
    return dico_cle




def str_to_utf(chaine):
    """
    Détermine les points de code UT8 d'une chaîne de caractères
    :param chaine: (str) Une chaîne de caractères
    :return: (list) Un tableau où chaque élément correspond au point de code UTF-8 d'un caractère de la chaîne
    :doctests:
        >>> str_to_utf("MESSAGE")
        [77, 69, 83, 83, 65, 71, 69]
        >>> str_to_utf("message")
        [109, 101, 115, 115, 97, 103, 101]
        >>> str_to_utf("")
        []
    """
    return [ord(c) for c in chaine]

def chiffrer(message, cle):
    """
    Chiffre un message par la méthode XOR avec la clé donnée
    :param message: (str) un message clair
    :param cle: (str) une clé de chiffrement
    :return: (str) le chiffré sous forme de points de code UTF-8 séparés par un espace
    :doctests:
        >>> chiffrer('MESSAGE', 'IAMAKEY')
        '4 4 30 18 10 2 28'
        >>> chiffrer('message', 'IAMAKEY')
        '36 36 62 50 42 34 60'
        >>> chiffrer('identificateur : 135674 - clé : fQ98c~m{)*e9+G!-', '(L%F')
        '65 40 64 40 92 37 67 47 75 45 81 35 93 62 5 124 8 125 22 115 30 123 17 102 5 108 70 42 193 108 31 102 78 29 28 126 75 50 72 61 1 102 64 127 3 11 4 107'
    """
    n = len(message)
    m = len(cle)
    
    clair = str_to_utf(message)
    cle_utf = str_to_utf(cle) * (n // m+1)
    
    
    chiffre = [ str(clair[i] ^ cle_utf[i]) for i in range(n)]
    
    return " ".join(chiffre)

def dechiffrer(message, cle):
    """
    Déchiffre un message par la méthode XOR avec la clé donnée
    :param message: (str) le chiffré sous forme de points de code UTF-8 séparés par un espace
    :param cle: (str) une clé de chiffrement
    :return: (str) le message clair
    :doctests:
        >>> dechiffrer('4 4 30 18 10 2 28', 'IAMAKEY')
        'MESSAGE'
        >>> dechiffrer('36 36 62 50 42 34 60', 'IAMAKEY')
        'message'
        >>> dechiffrer('65 40 64 40 92 37 67 47 75 45 81 35 93 62 5 124 8 125 22 115 30 123 17 102 5 108 70 42 193 108 31 102 78 29 28 126 75 50 72 61 1 102 64 127 3 11 4 107', '(L%F')
        'identificateur : 135674 - clé : fQ98c~m{)*e9+G!-'
    """
    chiffre = message.split(' ')
    n = len(chiffre)
    m = len(cle)
    
    cle_utf = str_to_utf(cle) * (n//m+1)
    
    clair = [ chr(int(chiffre[i]) ^ cle_utf[i]) for i in range(n)]
    
    return "".join(clair)


def chiffrer_fichier(n):
    """
    Chiffre les lignes du fichier par la méthode XOR avec une clé aléatoire de taille n
    :param n: (int) la taille de la clé
    :return: (None)
    :Effet de bord: Un fichier "cles_chiffre.txt" est créé contenant les n lignes du fichier d'entrée chacunes chiffrées par une clé
    """
    with open("cles.txt", "r", encoding="UTF-8") as fichier_e:
        with open("cles_chiffre.txt", "w", encoding="UTF-8") as fichier_s:
            for ligne in fichier_e.readlines():
                fichier_s.write(chiffrer(ligne))
    
    
    
## declaration des class

## fonction principal
def main():
    print(generer_cle(99))
    cles = generer_ensemble_cles(100,16)

    with open("cles.txt", "w", encoding="UTF-8") as fichier:
        for identificateur in cles:
            # \n permet de passer à la ligne.
            texte = "identificateur : {} - Clé : {} \n"
            ligne = texte.format(identificateur,
                                 cles[identificateur])
            fichier.write(ligne)
        fichier.close()
            
            
    with open("cles.txt", "r", encoding="UTF-8") as fichier:
        print(fichier.readlines())
        fichier.close()
        
    
    
    
    
        
## programme principal
if __name__ == '__main__':
    main()