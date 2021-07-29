import collections


#We go from root (head) to all leaves (employees).
# Since the procedure happens in parallel in tree branches,
# we need to return the longest time from head to a leaf.
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj=collections.defaultdict(list)
        self.res=0
        for i,v in enumerate(manager):
            adj[v].append(i)

        def dfs(manager,time):
            self.res=max(self.res,time)
            for emp in adj[manager]:
                dfs(emp,time+informTime[manager])

        dfs(headID,0)
        return self.res

