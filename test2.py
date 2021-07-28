import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(sec,target):
            seen.add((src,target))
            if src in seen:
                return False
            see.add(src)
            if src==target:
                return True
            ret=False
            for nei in adj[src]:
                ret=dfs(nei,target)
                if ret:
                    break

            return ret
        adj=collections.defaultdict(list)
        for i,j in edges:
            seen=set()
            if i in adj and j in adj and dfs(i,j):
                return i,j
            adj[i].append(j)
            adj[j].append(i)
