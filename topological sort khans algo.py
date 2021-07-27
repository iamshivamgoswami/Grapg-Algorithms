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


def topologicalSort(n,adj):
    in_degree=[0]*n
    for i in range(n):
        for j in adj[i]:
            in_degree[j]+=1

    q=collections.deque()
    for i in range(len(in_degree)):
        if in_degree[i]==0:
            q.append(i)


    cnt=0
    ans=[]
    while q:
        u=q.popleft()
        ans.append(u)
        for i in adj[u]:
            in_degree[i]-=1
            if in_degree[i]==0:
                q.append(i)

        cnt+=1
    #cycle
    if cnt!=n:
        return -1


    return ans



