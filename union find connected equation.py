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
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        return


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        A = uf(26)

        for i in equations:
            if i[1] == "=":
                a = ord(i[0]) - 97
                b = ord(i[-1]) - 97
                A.union(a, b)
        for i in equations:
            if i[1] == "!" and A.find(ord(i[0]) - 97) == A.find(ord(i[-1]) - 97):
                return False

        return True







