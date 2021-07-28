class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_v == root_u:
            return 0
        elif self.rank[root_v] < self.rank[root_u]:
            self.rank[root_u] += self.rank[root_v]
            self.parent[root_v] = root_u
        else:
            self.rank[root_v] += self.rank[root_u]
            self.parent[root_u] = root_v
        return 1


class Solution:

    def findCircleNum(self, mat: List[List[int]]) -> int:
        a = UnionFind(len(mat))
        count = len(mat)

        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]:
                    count -= a.union(i, j)

        return count


