import collections


class Solution(object):
    def canFinish(self, n, prerequisites):

        adj = collections.defaultdict(list)
        for i in prerequisites:
            adj[i[1]].append(i[0])
        in_degree = [0] * n
        n

        for i in range(n):
            for j in adj[i]:
                in_degree[j] += 1
        q = collections.deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        count = 0
        res = []
        while q:
            u = q.popleft()
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

            count += 1

        print(res)
        if not count == n:
            return False
        return True




