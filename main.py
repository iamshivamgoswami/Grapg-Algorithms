import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited=set()
        q=collections.deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))

        while q:
            x,y=q.popleft()
            for i,j  in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<len(mat ) and 0<=j<len(mat[0]) and (i,j) not in visited:
                    mat[i][j]=mat[x][y]+1
                    visited.add((i,j))
                    q.append((i,j))

        return mat
