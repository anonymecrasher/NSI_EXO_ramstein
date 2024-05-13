## importation des module

## declaration des fonction
def decaler_alphabet(n , alphabet):
    alphabet_r = []
    n %=len(alphabet)
    long = len(alphabet)
    for i in range(long):
        alphabet_r.append(alphabet[-long + i+ n])
    return alphabet_r

def chiffrer_lettre(lettre, alphabet_decale, alphabet):
    #i = 0
    #while lettre != alphabet[i]:
        #i += 1
    #return alphabet_decale[i]
    return alphabet_decale[alphabet.index(lettre)]

def chiffrer_mot(mot, alphabet_decale, alphabet):
    mot_r = ''
    for lettre in mot:
        mot_r += chiffrer_lettre(lettre, alphabet_decale, alphabet)
    return mot_r

def dechiffrer_lettre(lettre, alphabet_decale, alphabet):
    #i = 0
    #while lettre != alphabet[i]:
        #i += 1
    #return alphabet_decale[i]
    return alphabet[alphabet_decale.index(lettre)]

def dechiffrer_mot(mot, alphabet_decale, alphabet):
    mot_r = ''
    for lettre in mot:
        mot_r += dechiffrer_lettre(lettre, alphabet_decale, alphabet)
    return mot_r

def decrypter_mot(mot , alphabet):
    liste_r = []
    for i in range(len(alphabet)):
        liste_r.append(chiffrer_mot(mot,decaler_alphabet(i,alphabet),alphabet))
    return liste_r
## declaration des class

## fonction principal
def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    al = decaler_alphabet(3,alphabet)
    print(al)
    print(chiffrer_lettre('a',al,alphabet))
    print(chiffrer_mot('baba',al,alphabet))
    print(dechiffrer_mot('eded',al,alphabet))
    print(decrypter_mot('pneumonoultramicroscopicsilicovolcanoconiosis', alphabet))


## programme principal
if __name__ == '__main__':
    main()