## importation des modules
import random

## Déclaration des fonction
def table_generator():
    t = []
    for i in range(random.randint(3, 18)):
        t.append(random.randint(0, 256))
    return t

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
    
    t = table_generator()
    t = [random.randint(0,256) for i in range(random.randint(3,18))]
    print(t)
    print(average_table(t))




## Programme principal


if __name__ == '__main__':
    main()
