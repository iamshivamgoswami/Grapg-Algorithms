
import collections
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        h = [(0, 0)]
        visited = set()
        cost = 0
        while h:
            dist, curr_node = heapq.heappop(h)
            if curr_node not in visited:
                visited.add(curr_node)
                cost += dist
                for dist, neigh in graph[curr_node]:
                    if neigh not in visited:
                        heapq.heappush(h, (dist, neigh))

        return(cost)
