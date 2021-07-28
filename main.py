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
            if rank[y]>rank[x]:
                x,y=y,x

            parent[y]=x
            rank[x]+=rank[y]==rank[x]
            return 1
        count=0
        res=[]
        for i,j in positions:
            if (i,j ) not in parent:
                x=parent[x]=(i,j)
                count+=1
                rank[x]=0
                for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if y in parent:
                        count-=union(x,y)
            res.append(count)

        return res








