class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
        self.count = 0

    def isExist(self, u):
        return self.parent[u] >= 0

    def add(self, u):
        if self.isExist(u): return  # Only add if not existed yet!
        self.parent[u] = u
        self.size[u] = 1
        self.count += 1

    def find(self, u):
        if self.parent[u] == u: return u
        self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv: return False
        if self.size[pu] <= self.size[pv]:  # Merge the smaller component to the bigger component
            self.parent[pu] = pv  # Merge u into v
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu  # Merge v into u
            self.size[pu] += self.size[pv]
        self.count -= 1
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def getId(r, c):
            return r * n + c

        def neighbors(r, c):
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or not uf.isExist(getId(nr, nc)): continue
                yield getId(nr, nc)

        DIR = [0, 1, 0, -1, 0]
        uf = UnionFind(m * n)
        ans = [0] * len(positions)
        for i, (r, c) in enumerate(positions):
            curId = getId(r, c)
            uf.add(curId)  # Add new component if can
            for neiId in neighbors(r, c):
                uf.union(curId, neiId)
            ans[i] = uf.count

        return ans