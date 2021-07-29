import collections


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for i, v in enumerate(rooms):
            adj[i].extend(v)
        visited = set()

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        return len(visited) == len(rooms)

