adj=[ [0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
V=5



def minKey(key,visited,V):
    minn=float("inf")
    for v in range(V):
        if key[v]<minn and v not in visited:
            minn=key[v]
            min_index=v

    return min_index


def printMST( parent,V):
    print ("Edge ,Weight")
    for i in range(1, V):
        print( parent[i], "-", i, " ", adj[i][parent[i]])


def Mst(V,adj):
     key = [float("inf")] * V
     visited = set()
     key[0] = 0
     parent = [None] * V
     parent[0] = -1
     for i in range(V):
         u = minKey(key, visited, V)
         visited.add(u)
         for v in range(V):
             if adj[u][v] > 0 and v not in visited and key[v] > adj[u][v]:
                 key[v] = adj[u][v]

                 parent[v] = u
     return printMST(parent,V)




print(Mst(V,adj))