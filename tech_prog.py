## importation des module
import cv2
import numpy as np
import time
## declaration des fonction
def affiche_immage(image):
    img = cv2.imread(image)
    cv2.imshow('Super image de manchot', img)
    cv2.waitKey(0)
    cv2.destroyallwindows()
    
def rotation_image(image):
    if len(image) == 1:
        return image
    else:
        
        img = np.copy(image)
        
        long = len(img)
        mi = long//2
        so1 = np.copy(img[:mi,:mi])
        so2 = np.copy(img[mi:,:mi])
        so4 = np.copy(img[:mi,mi:])
        so3 = np.copy(img[mi:,mi:])
        so1,so2,so3,so4 = so4,so1,so2,so3
        so1,so2,so3,so4 = rotation_image(so1),rotation_image(so2), rotation_image(so3), rotation_image(so4)
        img[:mi,:mi],img[mi:,:mi],img[:mi,mi:],img[mi:,mi:] = so1,so2,so4,so3
        return img
    
def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_top_down(n, dico_solution_rencontrer):
    if n in dico_solution_rencontrer:
        return dico_solution_rencontrer[n]
    else:
        if n in (0,1):
            solution = n
            dico_solution_rencontrer[n] = solution
            return solution
        else:
            solution = fibonacci_top_down(n-1, dico_solution_rencontrer) + fibonacci_top_down(n-2, dico_solution_rencontrer)
            dico_solution_rencontrer[n] = solution
            return solution
        
def fibonacci_bottom_up(n, dico_solution_rencontrer):
    for i in range(n + 1):
        if i in (0,1):
            dico_solution_rencontrer[i] = i
        else:
            if i in dico_solution_rencontrer:
                pass
            else:
                dico_solution_rencontrer[i] = dico_solution_rencontrer[i - 1] + dico_solution_rencontrer[i - 2]
    return dico_solution_rencontrer[n]
            
  
def indice_plus_grande(valeur, systeme):
    i = 0
    while i < len(systeme) and valeur >= systeme[i]:
        i += 1
    return i - 1
  
def rendu_glouton_rec(valeur, systeme_monetaire):
    if valeur == 0:
        return []
    else:
        index = indice_plus_grande(valeur,systeme_monetaire)
        valeur -= systeme_monetaire[index]
        return [systeme_monetaire[index]] + rendu_glouton_rec(valeur,systeme_monetaire)
     
def rendu_recursif_top_down(valeur,systeme_monetaire):
    if valeur == 0:
        return []
    else:
        all_soluce = []
        index = indice_plus_grande(valeur,systeme_monetaire)
        for piece in range(index+1):
            all_soluce.append([systeme_monetaire[piece]]+[rendu_recursif_top_down(valeur-systeme_monetaire[piece],systeme_monetaire)])
            
        return all_soluce
    
def rendu_recursif_top_down_mem(valeur,systeme_monetaire,dico):
    if valeur == 0:
        return []
    elif valeur in dico:
        return dico[valeur]
    else:
        all_soluce = []
        index = indice_plus_grande(valeur,systeme_monetaire)
        for piece in range(index+1):
            resultat =  [systeme_monetaire[piece]]+[rendu_recursif_top_down_mem(valeur-systeme_monetaire[piece],systeme_monetaire,dico)]
            all_soluce.append(resultat)
        dico[valeur] = all_soluce.copy()
        return all_soluce
            

def _calul_plus_grand_piece(valeur,systeme_monetaire):
    for i in range(len(systeme_monetaire)):
        if valeur > systeme_monetaire[-i]:
            return systeme_monetaire[:len(systeme_monetaire)-i]
def rendu_bottom_up(valeur,systeme_monetaire):
        sol = [[[]],[[1]]]
        for i in range(2,valeur+1):
            pgcd = _calul_plus_grand_piece(valeur,systeme_monetaire)
            print(pgcd)
            sol.append([])
            for y in pgcd:
                sol[i].append([y] + sol[i - y])
        return sol
                
            
            
        
    
    
## declaration de class

## fonction principal
def main():
    #img = np.copy(cv2.imread("manchot.png"))
    #cv2.imshow('', rotation_image(img))
    #cv2.waitKey(0)
    #cv2.destroyallwindows()
    #dico_solution_rencontrer = {}
    #for i in range(35):
        #t1 = time.perf_counter_ns()
        #fibonacci_bottom_up(i,dico_solution_rencontrer)
        #t2 = time.perf_counter_ns()
        #print(t2 - t1)
    sys = [1,2,5,10]
    dico = {}
    for i in range(15):
        t1 = time.perf_counter_ns()
        rendu_recursif_top_down(i,sys)
        t2 = time.perf_counter_ns()
        print(t2 - t1)
    print('change')
    for i in range(10):
        t1 = time.perf_counter_ns()
        rendu_bottom_up(i,sys)
        t2 = time.perf_counter_ns()
        print(t2 - t1)
        print(rendu_bottom_up(i,sys))
        
        

## programme principal
if __name__ == '__main__':
    main()
