## importation des module

## declaration des fonction
def chaine_to_utf(chaine):
    text = []
    for carac in chaine:
        text.append(ord(carac))
    return text


def chiffre_dechiffre(message, masque):
    liste = ''
    code = chaine_to_utf(message)
    masq = chaine_to_utf(masque)
    print(code)
    for i in range(len(code)):
        liste += chr(code[i] ^ masq[i])
    return liste
    

## declaration des class

## fonction principal
def main():
    masque = "CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES"
    masque2 = chiffre_dechiffre("CETTEPHRASEESTVRAIMENTTRESTRESLONGUEMAISCESTFAITEXPRES",masque[::-1])
    print(masque2)
    print(chaine_to_utf('baba'))
    print(chiffre_dechiffre('et au sa va',masque))
    print(chiffre_dechiffre('&1t50p;3a%$',masque[::-1]))
    
    print(chiffre_dechiffre('et au sa va',masque2))
    

## programme principal
if __name__ == '__main__':
    main()