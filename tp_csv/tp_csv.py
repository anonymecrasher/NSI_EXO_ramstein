# importation des modules
import csv

# Déclaration des fonction

# declaration des class

# fonction principal
def main():
    fichier = open('echantillon_taille_t_shirt.csv', newline='', encoding='utf-8')
    table = csv.DictReader(fichier, delimiter=',')
    table = [dict(ligne) for ligne in table]

# Programme principal
if __name__ == '__main__':
    main()