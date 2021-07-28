# For each edge {a, b}, check if a is connected to b
# or not. If found to be false, connect them by appending
# their top parents.
class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u, v):

        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return 0  # Return False if u and v are already union
        if self.rank[root_u] < self.rank[root_v]:
            self.rank[root_v] += self.rank[root_u]
            self.parent[root_u] = root_v

        else:
            self.rank[root_u] += self.rank[root_v]
            self.parent[root_v] = root_u
        return 1
class Solution:
    def numIslands2(self, m, n, positions):
        count=0
        res=[]
        for i,j in positions:
            count+=1
            a=unionFind(count)
            x=(i,j)
            for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                count-=a.union(x,y)
            res.append(count)

        return res