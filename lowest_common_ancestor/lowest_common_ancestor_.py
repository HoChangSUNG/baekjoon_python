# 가장 가까운 공통 조상, 3584번
import sys
sys.setrecursionlimit(100000)

def dfs(x,depth):
    d[x]=depth
    for y in graph[x]:
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

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    d = [0]*(n+1)
    parent=[i for i in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a,b = map(int,sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        parent[b]=a

    root=1
    for i in range(1,n+1): #루트 찾기
        if parent[i]==i:
            root = i
            break

    dfs(root,0)
    a,b = map(int,sys.stdin.readline().rstrip().split())
    print(lca(a,b))
