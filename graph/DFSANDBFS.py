#dfs와 bfs, 1260번
import sys
from collections import deque
def dfs(node):
    visited[node]=True
    print(node,end=' ')
    for adjNode in graph[node]:
        if not visited[adjNode]:
            dfs(adjNode)

def bfs(startNode):
    queue = deque()
    queue.append(startNode)
    visited[startNode]=True
    while queue:
        curNode = queue.popleft()
        print(curNode,end=' ')
        for adjNode in graph[curNode]:
            if not visited[adjNode]:
                queue.append(adjNode)
                visited[adjNode]=True

n,m,v =map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()

dfs(v)
visited = [False]*(n+1)
print()
bfs(v)