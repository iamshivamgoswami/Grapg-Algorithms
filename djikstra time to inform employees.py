import collections
import heapq

#We go from root (head) to all leaves (employees).
# Since the procedure happens in parallel in tree branches,
# we need to return the longest time from head to a leaf.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj=collections.defaultdict(list)
        for i,managerid in enumerate(manager):
            adj[managerid].append((informTime[i],i))
        dist={}
        heap=[(informTime[headID],headID)]
        while heap:
            time,u=heapq.heappop(heap)
            if u in dist:
                continue
            dist[u]+=time
            for w,v in adj[u]:
                if v in dist:
                    continue
                heapq.heappush(heap,(time+w,v))

        return max(dist.values())


