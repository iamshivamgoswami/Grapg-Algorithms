#The idea is to simply build the graph by adding
# one edge at a time, and running DFS to see if a
# path already exists between the two nodes. If it does,
# the edge in consideration is redundant.
import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)
        def dfs(src ,dst):
            if src in seen:
                return False
            if src not in seen:
                seen.add(src)
                if src==dst:
                    return True
                ret=False
                for nei in adj[src]:
                    ret=dfs(nei,dst)
                    if ret:
                        breakin


                return ret


        for u,v in edges:
            seen=set()
            if u in adj and v in adj and dfs(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)



