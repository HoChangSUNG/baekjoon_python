# 효율적인 해킹, 1325번
import sys
from collections import deque

def bfs(v):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append(v)
    visited[v]=True
    count=1
    while queue:
        q = queue.popleft()
        for i in adjlist[q]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                count += 1
    return count

n,m = map(int,sys.stdin.readline().rstrip().split())
adjlist = [[]for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    adjlist[b].append(a)

result=[0]
max=0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt>max:
        max=cnt
    result.append(cnt)
for i in range(n+1):
    if result[i] == max:
        print(i,end=' ')


