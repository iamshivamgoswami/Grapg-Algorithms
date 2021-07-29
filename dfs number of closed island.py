class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            grid[i][j] = 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 0 and (x, y) not in visited:
                    dfs(x, y)

        count = 0
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:

                    if (i, j) not in visited and grid[i][j] == 0:
                        count += 1
                        dfs(i, j)

        visited = set()
        c = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 0:
                    dfs(i, j)
                    c += 1

        return c




