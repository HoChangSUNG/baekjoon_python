import sys
sys.setrecursionlimit(10**9)

def dfs(node):
    visited[node]=True
    dp[node][0]=0
    dp[node][1]=1
    for adjNode in graph[node]:
        if not visited[adjNode]:
            dfs(adjNode)
            dp[node][0]+=dp[adjNode][1]
            dp[node][1]+= min(dp[adjNode][0],dp[adjNode][1])

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

dp=[[0,0] for _ in range(n+1)]
visited=[False]*(n+1)
dfs(1)
print(min(dp[1][0],dp[1][1]))