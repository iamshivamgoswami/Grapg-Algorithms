class Solution:

    def findCircleNum(self, mat: List[List[int]]) -> int:
        def connected(mat):
            visited = set()
            count = 0
            for i in range(len(mat)):
                if i not in visited:
                    dfs(i, visited, mat)
                    count += 1

            return count

        def dfs(v, visited, mat):
            visited.add(v)
            for j in range(len(mat)):
                if mat[v][j] == 1:
                    if j not in visited:
                        dfs(j, visited, mat)
        return connected(mat)

