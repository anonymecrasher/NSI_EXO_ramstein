## importation des module

## declaration des fonction
def voisins_entrants(adj,x):
    """
    fonction renvoyant la liste des predeceseur de x dans le graphe adj
    @input adj:type = list
    @input x:type = int
    @output r:type = list
    
    """
    r = []
    for i in range(len(adj)):
        if x in adj[i]:
            r.append(i)
    return r

## declaration des classe

## fonction principal
def main():
    adj = [[1,2], [2], [0], [0]]
    print(adj[0])
    print(adj[2])
    # il smeble que sela coresponde a la liste des successeurs
    print(voisins_entrants(adj, 0))
    print(voisins_entrants(adj, 1))
## programme princpal
if __name__ == '__main__':
    main()