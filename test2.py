import collections


class Solution:
    def removeStones(self, mat: List[List[int]]) -> int:
        def dfs(i,j):
            points.remove((i,j))
            for y in row[i]:
                if (i,y) in points:
                    dfs(i,y)
            for x in cols[j]:
                if (x,j) in points:
                    dfs(x,j)


        points={(i,j) for i,j in mat}
        island=0
        row=collections.defaultdict(list)
        cols=collections.defaultdict(list)
        for i,j in mat:
            row[i].append(j)
            cols[j].append(i)


        for i,j in mat:
            if (i,j) in points:
                dfs(i,j)
                island+=1
        return len(mat)-island







