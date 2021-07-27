class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        adj = [[] for i in range(n)]
        for i, j in connections:
            adj[i].append(j)
            adj[j].append(i)

        def connect(adj, n):
            visited = set()
            count = 0
            for v in range(n):
                if v not in visited:
                    dfs(v, visited)
                    count += 1

            return count

        def dfs(v, visited):
            visited.add(v)
            for u in adj[v]:
                if u not in visited:
                    dfs(u, visited)

        return (connect(adj, n))-1