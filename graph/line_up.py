# 줄세우기, 2252번
import sys

def dfs(v):
    visited[v]=True
    for adjvertex in adj_graph[v]:
        if not visited[adjvertex]:
            dfs(adjvertex)
    result.append(v)

n,m = map(int,sys.stdin.readline().rstrip().split())
adj_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adj_graph[a].append(b)
visited = [False for _ in range(n+1)]

result =[]
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

result.reverse()
for i in result:
    print(i,end=' ')

