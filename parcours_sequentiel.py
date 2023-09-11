## importation des modules


## Déclaration des fonction


def somme_tableau(t):
    ans = 0
    for i in t:
        ans += int(i)
    return ans

def average_table(t):
    ans = somme_tableau(t)
    ans = ans /len(t)
    return ans
def main():
    
    t = [5,8,12,1,6,14,13,22,3,87]
    average_table(t)

if __name__ == '__main__':
    main()
