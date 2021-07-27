import collections
import heapq
import math


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        adj = collections.defaultdict(list)
        for i, cost in enumerate(wells):
            adj[0].append((cost, i + 1))
        for i, j, k in pipes:
            adj[i].append((k, j))
            adj[j].append((k, i))

        heapq.heapify(adj[0])
        h = adj[0]
        cost = 0

        visited = set([0])
        while len(visited) < n + 1:
            dist, curr_node = heapq.heappop(h)

            if curr_node not in visited:
                visited.add(curr_node)

                cost += dist

                for i in adj[curr_node]:
                    new_node = i[1]
                    new_dist = i[0]
                    if new_node not in visited:
                        heapq.heappush(h, (new_dist, new_node))
        return (cost)