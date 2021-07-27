import collections
import heapq
import math


def func():
    n = 5
    edges =[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
    k= 2
    adj = collections.defaultdict(list)
    for u,v,w in edges:
        adj[u].append([v,w])
        adj[v].append([u,w])

    def Djikstra(city):
        heap=[(0,city)]
        dist={}
        while heap:
            currW,u=heapq.heappop(heap)
            if u in dist:
                continue
            if u!=city:
                dist[u]=currW
            for v,w in adj[u]:
                if v in dist:
                    continue
                if currW+w<=k:
                    heapq.heappush(heap,(currW+w,v))

        return len(dist)
    res=[]
    for city in range(n):
        res.append([Djikstra(city),city])
    res.sort()
    maxx=-math.inf
    a=res[0][0]
    for i in res:
        if i[0]==a:
            maxx=max(maxx,i[1])

    return maxx




print(func())
