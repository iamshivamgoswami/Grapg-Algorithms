# User function Template for python3


class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        def func(adj):
            visited = set()
            n = len(adj)



            def dfs(v, memo={}):
                visited.add(v)

                for nei in adj[v]:
                    if nei not in visited:
                        if dfs( nei,memo):
                            memo[nei] = True
                            return True
                    elif memo[nei]:
                        return True

                memo[v] = False

            for node in range(n):
                if node not in visited:
                    if dfs(node):
                        return True

            return False


