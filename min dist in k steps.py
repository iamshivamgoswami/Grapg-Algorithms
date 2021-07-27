import collections
import heapq
# Using a set for 'seen' will prevent us from finding solutions
# with a lesser number of stops. Using a hashmap (node -> no
# of stops to destination) we can only explore seen nodes which
# will result in a lesser no of stops(Though with a higher distance).

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        pq, seen = [(0, src, k + 1)], {}
        while pq:
            d, u, s = heapq.heappop(pq)
            if u == dst:
                return d
            if u in seen and seen[u] >= s:
                continue
            seen[u] = s
            if s:
                for v, w in graph[u]:
                    heapq.heappush(pq, (d + w, v, s - 1))
        return -1

