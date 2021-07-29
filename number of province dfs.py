class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:

        def dfs(v, visited):
            visited.add(v)
            for j in range(len(mat[0])):
                if mat[v][j]:
                    if j not in visited:
                        dfs(j, visited)

        visited = set()
        count = 0
        for i in range(len(mat)):
            if i not in visited:
                dfs(i, visited)
                count += 1
        return count


w