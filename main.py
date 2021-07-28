
class Solution:
    def numIslands2(self, m, n, positions):
        parent,rank={},{}
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            x,y=find(x),find(y)
            if x==y:
                return 0
            if rank[x]<rank[y]:
                x,y=y,x

            rank[x]+=rank[x]==rank[y]
            return 1
        counts,count=[],0

        for i,j in positions:
            if (i,j) not in parent:
                x=parent[x]=i,j
                rank[x]=0
                count+=1
                for y in