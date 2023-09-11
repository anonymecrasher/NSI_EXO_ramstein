## importation des modules


## Déclaration des fonction


def somme_tableau(t):
    ans = 0
    for i in t:
        ans += int(i)
    return ans

def average_table(t):
    """
    doc ...
    """
    ans = somme_tableau(t)
    ans = ans /len(t)
    return ans
def main():
    
    help(average_table)
    
    t = [5,8,12,1,6,14,13,22,3,87]
    print(average_table(t))




## Programme principal


if __name__ == '__main__':
    main()
