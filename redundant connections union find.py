class uf:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_y == root_x:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x

            self.rank[root_x] += self.rank[root_y]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        a = uf(len(edges))
        visited = set()
        for i, v in edges:
            if (i, v) in visited:
                continue

            visited.add((i, v))
            if not a.union(i - 1, v - 1):
                return i, v




