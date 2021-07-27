# use khans algo of topological sort which
# is applicable on adg.There’s a simple proof
# to the above fact is that a DAG does not contain
# a cycle which means that all paths will be of
# finite length.Since S is the longest path there
# can be no incoming edge to u and no outgoing edge
# from v, if this situation had occurred then S
# would not have been the longest path
# => indegree(u) = 0 and outdegree(v) = 0
import collections

mat=[[4], [2], [1, 3], [2, 4], [0, 1, 3]]
d=collections.defaultdict(set)
adj=collections.defaultdict(list)
for i,v in enumerate(mat):
    for j in v:
        d[i].add(j)
        if i not in d[j]:
            adj[i].append(j)
print(adj)

def isCyclic(n,adj):
    in_degree=[0]*n

    for i in range(n):
        for j in adj[i]:
            in_degree[j]+=1
    q=collections.deque()
    for i in range(len(in_degree)):
        if in_degree[i]==0:
            q.append(i)

    cnt=0
    while q:
        nu=q.popleft()
        for v in adj[nu]:
            in_degree[v]-=1
            if in_degree[v]==0:
                q.append(v)
        cnt+=1
    return cnt


print(isCyclic(len(mat),adj)==len(mat))

