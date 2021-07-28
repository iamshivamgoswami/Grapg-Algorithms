#The idea is to simply build the graph by adding
# one edge at a time, and running DFS to see if a
# path already exists between the two nodes. If it does,
# the edge in consideration is redundant.
import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)



