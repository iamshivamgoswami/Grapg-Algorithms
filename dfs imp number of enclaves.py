class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        count = 0
        ones = 0

        def dfs(i, j):
            nonlocal count
            visited.add((i, j))
            if grid[i][j] == 1:
                count += 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 1 <= x < n - 1 and 1 <= y < m - 1:

                    if (x, y) not in visited and grid[x][y]:
                        dfs(x, y)

        d = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ones += 1

                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    if grid[i][j]:
                        dfs(i, j)

        return ones - count




