## importation des modules


## Déclaration des fonction

def somme(n):
    ans = 0
    for i in range(n+1):
        ans += i
    return ans

def somme_tableau(t):
    ans = 0
    for i in t:
        ans += int(i)
    return ans
        
    
    
    

## programme principale
t = (5, 5, 5, 9, 1, 1)
resultat = somme_tableau(t)
print(resultat)
