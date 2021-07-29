class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxx = 0
        visited = set()

        def dfs(i, j):
            nonlocal count
            if (i, j) in visited:
                return
            count += 1

            self.maxx = max(self.maxx, count)
            visited.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    dfs(x, y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = 0
                    dfs(i, j)

        return self.maxx


