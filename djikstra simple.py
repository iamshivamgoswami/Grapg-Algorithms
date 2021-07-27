# dist={2: 0, 1: 1, 3: 1, 4: 2}
class Solution(object):
    def networkDelayTime(self, mat, n, k):
        adj = collections.defaultdict(list)
        for i, j, w in mat:
            adj[i].append((j, w))

        h = [(0, k)]
        visited = {}

        while h:
            dist, curr_node = heapq.heappop(h)
            if curr_node in visited:
                continue
            visited[curr_node] = dist
            for nei, d2 in adj[curr_node]:
                if nei not in visited:
                    heapq.heappush(h, (dist + d2, nei))

        return max(visited.values()) if len(visited) == n else -1
