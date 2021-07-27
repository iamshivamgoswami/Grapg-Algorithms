
import collections
class Subset:
    def __init__(self,parent,rank):
        self.parent=parent
        self.rank=rank
mat=[[4], [2, 4], [1, 3], [2, 4], [0, 1, 3]]
d=collections.defaultdict(set)
adj=collections.defaultdict(list)
for i,v in enumerate(mat):
    for j in v:
        d[i].add(j)
        if i not in d[j]:
            adj[i].append(j)


print(adj)

def find(subsets,node):
    if subsets[node].parent!=node:
        subsets[node].parent=find(subsets,subsets[node].parent)
    return subsets[node].parent
def union(subsets,u,v):
    if subsets[u].rank<subsets[v].rank:
        subsets[u].parent=v
    elif subsets[u].rank>subsets[v].rank:
        subsets[v].parent=u
    else:
        subsets[v].parent=u
        subsets[u].rank+=1

def iscyclic(V,adj):
    subsets=[]
    for u in range(V):
        subsets.append(Subset(u,0))
    for u in adj:
        u_rep=find(subsets,u)
        for v in adj[u]:
            v_rep=find(subsets,v)

            if v_rep==u_rep:
                return True
            else:
                union(subsets,u_rep,v_rep)
    return False



V=len(mat)
print(iscyclic(V,adj))






