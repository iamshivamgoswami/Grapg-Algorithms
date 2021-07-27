# Prim’s algorithm assumes that all vertices
# are connected. But in a directed graph, every
# node is not reachable from every other node.
# So, Prim’s algorithm fails due to this reason.
import heapq

adj=[[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]


h=[(0,0)]
visited=set()
cost=0
while h:
    dist,curr_node=heapq.heappop(h)
    if curr_node not in visited:
        visited.add(curr_node)
        cost+=dist
        for i in adj[curr_node]:
            new_dist=i[1]
            new_node=i[0]
            if new_node not in visited:
                heapq.heappush(h,(new_dist,new_node))


print(cost)
