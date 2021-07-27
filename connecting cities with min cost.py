import heapq
import collections


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        for i, j, k in connections:
            adj[i].append((j, k))
            adj[j].append((i, k))
        h = [(0, 1)]
        visited = set()
        cost = 0
        while h:
            dist, curr_node = heapq.heappop(h)
            if curr_node not in visited:
                visited.add(curr_node)
                cost += dist
                for i in adj[curr_node]:
                    new_dist = i[1]
                    new_node = i[0]
                    if new_node not in visited:
                        heapq.heappush(h, (new_dist, new_node))

        return (cost) if len(visited) == n else -1



