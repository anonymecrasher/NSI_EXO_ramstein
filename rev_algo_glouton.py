## Importation des modules

## declaration des consante
emsemble_des_piece = [1, 2, 5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000]

## Déclaration des fonctions
def rendu_money(argent):
    argent *= 100
    ren = []
    for i in range(len(emsemble_des_piece)-1,0,-1):
        
        temp = argent - emsemble_des_piece[i]
        if temp < 0:
            ren.append(0)
        else:
            if temp -emsemble_des_piece[i] >= 0:
                ren.append(2)
                argent = temp - emsemble_des_piece[i]
            else:
                ren.append(1)
                argent = temp
    return ren

def int_rendu_money(argent):
    ren = rendu_money(argent)
    aff =[]
    emsemble_des_piece.reverse()
    for i in range(len(emsemble_des_piece)-1):
        if ren[i] > 0:
            print(ren[i])
            print(emsemble_des_piece[i])
            if emsemble_des_piece[i] >= 100:
                aff.append(str(ren[i])+"*" + str(round(emsemble_des_piece[i]/100))+ " euros")
            else:
                a = str(ren[i]) + "*" + str(emsemble_des_piece[i]) + " centimes"
                aff.append(a)
    return aff
                
    

## Déclaration des classes

## fonction principale
def main():
    print(rendu_money(145.12))
    print(int_rendu_money(145.12))

## Programme principal
if __name__ == '__main__':
    main()
