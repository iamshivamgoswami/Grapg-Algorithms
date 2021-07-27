mat=[[2, 3], [0], [1], [4], []]
def connected_components(mat):
    flag=set()
    n=len(mat)
    count=0
    for v in range(n):
        if v not in flag:
            dfs(v,flag)
            count+=1
    return count


def dfs(v,flag):
    flag.add(v)
    for u in mat[v]:
        if u not in flag:
            dfs(u,flag)



print(connected_components(mat))