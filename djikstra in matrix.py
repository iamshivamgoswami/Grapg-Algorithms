import heapq
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        def func():
            dest = tuple(destination)
            m = len(maze)
            n = len(maze[0])

            def go(start, directions):
                i, j = start
                ii, jj = directions
                l = 0
                while 0 <= i + ii < m and 0 <= j + jj < n and maze[i + ii][j + jj] != 1:
                    i += ii
                    j += jj
                    l += 1
                return l, (i, j)

            visited = {}
            h = []
            heapq.heappush(h, (0, tuple(start)))
            while h:
                l, curr_node = heapq.heappop(h)
                if curr_node in visited and visited[curr_node] <= l:
                    continue
                visited[curr_node] = l
                if curr_node == dest:
                    return l
                for directions in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    le, np = go(curr_node, directions)
                    heapq.heappush(h, (l + le, np))
            return -1
        return func()

