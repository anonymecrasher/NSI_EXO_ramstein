# importation des modulles
import functools
import random

# declaration des fonctions

# declaration des fonctions

# fonction principal
def main():
    liste = functools.reduce(lambda acc,x: acc + x,[random.randint(0,100) for i in range(20)])
    print(liste)
    print(functools.reduce(lambda acc, x: acc + 1,[random.randint(0,100) for i in range(20)],0))
    
# programme principal
if __name__ == '__main__':
    main()
