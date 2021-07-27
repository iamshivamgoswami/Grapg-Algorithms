import collections
import heapq

n = 3
edges = [[0,1]]
succProb = [0.5]
start = 0
end = 2
def func():
    adj=collections.defaultdict(list)
    for i,v in enumerate(edges):
        adj[v[0]].append((v[1],succProb[i]))
        adj[v[1]].append((v[0], succProb[i]))


    h=[(-1,start)]
    cost=1
    visited={}
    while h:
        dis,curr_node=heapq.heappop(h)

        if curr_node not in visited:

            visited[curr_node]=dis
            for i in adj[curr_node]:
                new_dist,new_node=i[1],i[0]
                if new_node not in visited:
                    heapq.heappush(h,(new_dist*dis,new_node))


    return visited[end]*-1 if end in visited else -1

print(func())
