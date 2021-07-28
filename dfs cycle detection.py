#The idea is to simply build the graph by adding
# one edge at a time, and running DFS to see if a
# path already exists between the two nodes. If it does,
# the edge in consideration is redundant.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(set)
        def dfs(source,target):
            if source not in seen:
                seen.add(source)
                if source==target:
                    return True
                return any (dfs(nei,target)for nei in graph[source])
        for u,v in edges:

            graph[u].add(v)
            graph[v].add(u)
        for u,v in edges:
            seen=set()
            if u in graph and v in graph and dfs(u,v):
                return u,v