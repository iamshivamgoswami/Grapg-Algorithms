class Subset:
    def __init__(self,par,rank):
        self.parent=par
        self.rank=rank

mat=[[1,1,0],[1,1,0],[0,0,1]]
def find(subset,node):
    if subset[node].parent!=node:
        subset[node].parent=find(subset,subset[node].parent)

    return subset[node].parent
def union(subsets,u,v):
    if subsets[u].rank>subsets[v].rank:
        subsets[v].parent=u
    elif subsets[u].rank<subsets[v].rank:
        subsets[u].parent=v
    else:
        subsets[u].parent = v
        subsets[v].rank+=1

def isCyclic(n,mat):
    subsets=[]
    for u in range(n):
        subsets.append(Subset(u,0))

    for u in adj:
        u_parent=find(subsets,u)
        for v in adj[u]:
            v_parent=find(subsets,u)
            if v_parent==u_parent:
                return True

            else:
                union(subsets,u_parent,v_parent)



