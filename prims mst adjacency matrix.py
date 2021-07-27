

def minKey(key,mstSet,v):
    minn = float("inf")
    for i in range(v):

        if key[i]<minn and mstSet[i]==False:
            minn=key[i]
            min_index=i

    return min_index


def Mst(v,adj):
    key=[float("inf")]*v
    key[0]=0
    mstSet=[False]*v
    for i in range(v):
        u=minKey(key,mstSet,v)
        mstSet[u]=True
        for i in range(v):
            if adj[u][i]>0 and mstSet[i]==False and key[i]>adj[u][i]:
                key[i]=adj[u][i]
    return key
adj=[[0,5,1],[5,0,3],[1,3,0]]
v=3

print(sum(Mst(v,adj)))