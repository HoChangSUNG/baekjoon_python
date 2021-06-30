# 선수과목(Prerequisite), 14567번
import sys
from collections import deque

def tsort():
    queue =deque()
    for i in range(1,n+1):
        if in_degree[i]==0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:
            in_degree[adj_node]-=1
            dp[adj_node] = max(dp[node]+1,dp[adj_node])
            if in_degree[adj_node]==0:
                queue.append(adj_node)

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [[]for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
dp = [1 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    in_degree[b]+=1
tsort()
print(*dp[1:])