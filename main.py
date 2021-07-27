# if there is no path mat[i][j]==-1 then check if there is path through k
class Solution:
    def shortest_distance(self, mat):

        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if mat[i][k] == -1 or mat[k][j] == -1:
                        continue
                    elif mat[i][j] == -1:
                        mat[i][j] = mat[i][k] + mat[k][j]
                    else:

                        mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        return mat