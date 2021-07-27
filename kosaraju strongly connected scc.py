adj=[[2, 3], [0], [1], [4], []]
def dfsUtil(v,visited,adj):
    visited.add(v)
    print(v,end=" ")
    for i in adj[v]:
        if i not in visited:
            dfsUtil(i,visited,adj)

def fillOrder(v,visited,stack):
    visited.add(v)
    for i in adj[v]:
        if i not in visited:
            fillOrder(i,visited,stack)

    stack.append(v)
def getTranspose(adj):

    g=[[] for i in range(len(adj))]
    for i,v  in enumerate(adj):
        for j in v:

            g[j].append(i)




    return g

def printScc(adj):
    stack=[]
    visited=set()
    for i in range(len(adj)):
        if i not in visited:
            fillOrder(i,visited,stack)
    gt=getTranspose(adj)
    visited=set()
    count=0
    while stack:
        i=stack.pop()
        if i not in visited:
            dfsUtil(i,visited,gt)

            print(" ")

print(printScc(adj))


