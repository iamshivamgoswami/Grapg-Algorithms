class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return False  # Return False if u and v are already union
        if self.rank[root_u] < self.rank[root_v]:
            self.rank[root_v] += self.rank[root_u]
            self.parent[root_u] = root_v
        else:
            self.rank[root_u] += self.rank[root_v]
            self.parent[root_v] = root_u
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = unionFind(n)
        for u, v in edges:
            if not uf.union(u - 1, v - 1):
                return u, v

