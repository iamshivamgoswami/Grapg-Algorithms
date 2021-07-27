class Solution:
    def isNegativeWeightCycle(self, n, edges):
        dis = [float("inf")] * n
        dis[0] = 0
        for i in range(n - 1):
            for u, v, w in edges:
                if dis[u] != float("inf") and dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w

            for u, v, w in edges:
                if dis[u] != float("inf ") and dis[u] + w < dis[v]:
                    print("negative cycle")
                    return 1
        return 0




