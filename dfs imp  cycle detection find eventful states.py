class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited=[-1]*len(graph)
        n=len(graph)
        res=[]
        def dfs(i):
            visited[i]=0
            for v in graph[i]:
                if visited[v]==0 or (visited[v]==-1 and dfs(v)):
                    return True

            visited[i]=1 #marked safe and for future use

            res.append(i)
            return False

        for i in range(n):
            if visited[i]==-1:
                dfs(i)
        return sorted(res)





