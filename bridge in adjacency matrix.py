import collections
class Solution:
    rank = {}
    graph = collections.defaultdict(list)
    conn_dict = {}

    def criticalConnections(self, n, mat) :

        self.formGraph(n, mat)
        print(self.graph)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node, discovery_rank):

        # That means this node is already visited. We simply return the rank.
        if self.rank[node]:
            return self.rank[node]

        # Update the rank of this node.
        self.rank[node] = discovery_rank

        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:

            # Skip the parent.
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            # Recurse on the neighbor.
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def formGraph(self, n, mat):

        # Reinitialize for each test case
        self.rank = {}
        self.graph = collections.defaultdict(list)
        self.conn_dict = {}

        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    self.graph[i].append(j)

                    self.conn_dict[(min(i, j), max(i, j))] = 1
mat=[[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]

n=5
a=Solution()
print(a.criticalConnections(n,mat))