## importation des module

## declaration des fonction
def find_hamiltonian_path(graph, start, visited, path):
    visited[start] = True
    path.append(start)

    if len(path) == len(graph):
        return True

    for neighbor in graph[start]:
        if not visited[neighbor]:
            if find_hamiltonian_path(graph, neighbor, visited, path):
                return True

    path.pop()
    visited[start] = False
    return False

def hamiltonian_path(graph):
    start_node = list(graph.keys())[0]
    num_nodes = len(graph)
    visited = {node: False for node in graph}
    path = []

    if find_hamiltonian_path(graph, start_node, visited, path):
        return path
    else:
        return "No Hamiltonian path exists in the given graph"




## declaration des class
        
## fonction principal
def main():
    amerique_sud = {
        'France':['Bresil','Suriname'],
        'Suriname':['France','Bresil','Guyana'],
        'Guyana':['Venezuela','Bresil','Suriname'],
        'Venezuela':['Guyana','Bresil','Colombie'],
        'Colombie':['Venezuela','Bresil','Equateur','Perou'],
        'Equateur':['Colombie','Perou'],
        'Perou':['Bolivie','Bresil','Equateur','Colombie'],
        'Bolivie':['Perou','Bresil','Paraguay','Argentine','Chili'],
        'Paraguay':['Bolivie','Argentine','Bresil'],
        'Chili':['Bolivie','Argentine'],
        'Argentine':['Chili','Bolivie','Paraguay','Bresil','Uruguay'],
        'Uruguay':['Argentine','Bresil'],
        'Bresil':['France','Suriname','Guyana','Venezuela','Colombie','Perou','Bolivie','Paraguay','Argentine','Uruguay']
        }
    
    print(hamiltonian_path(amerique_sud))

## programme principal
if __name__ == '__main__':
    main()