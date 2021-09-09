#LCA, 11437번
import sys
sys.setrecursionlimit(100000)
def dfs(x,depth):
    d[x]=depth
    c[x]=True
    for y in graph[x]:
        if c[y]:
            continue
        parent[y]=x
        dfs(y,depth+1)

def lca(a,b):
    while d[a]!=d[b]:
        if d[a]>d[b]:
            a=parent[a]
        else:
            b=parent[b]
    while a!=b:
        a = parent[a]
        b = parent[b]
    return a

n = int(sys.stdin.readline().rstrip())
d = [0]*(n+1)
c = [0]*(n+1)
parent=[0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1,0)
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(lca(a,b))
