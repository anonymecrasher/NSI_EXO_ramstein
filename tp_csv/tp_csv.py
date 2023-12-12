# importation des modules
import csv

# Déclaration des fonction
def distance_euclidienne(ob1,ob2):
    return ((ob1['Taille (cm)'] - ob2['Taille (cm)'])**2+ (ob1['Poids (kg)'] - ob2['Poids (kg)'])**2)**(1/2)

def calcul_distance(ob, list_ob):
    for i in list_ob:
        i['distance'] = distance_euclidienne(ob,i)
    return list_ob

def compte_voisins(list_ob):
    temp = []
    temp2 = []
    for i in list_ob:
        temp.append([i['distance'],i['Taille T Shirt']])
    temp.sort()
    m,l = 0,0
    for i in temp:
        if i[1] == 'M':
            m += 1
        if i[1] == 'L':
            l += 1
        temp2.append([m,l])
    return temp2
            

# declaration des class

# fonction principal
def main():
    fichier = open('echantillon_taille_t_shirt.csv', newline='', encoding='utf-8')
    table = csv.DictReader(fichier, delimiter=',')
    table = [dict(ligne) for ligne in table]
    
    fichier.close()
    
    for objet in table:
        objet['Taille (cm)'] =  int(objet['Taille (cm)'])
        objet['Poids (kg)'] = int(objet['Poids (kg)'])
    print(distance_euclidienne(table[1],table[5]))
    table = calcul_distance({'Taille (cm)':161, 'Poids (kg)':61},table)
    for i in compte_voisins(table):
        print(i)
    
    
        

# Programme principal
if __name__ == '__main__':
    main()