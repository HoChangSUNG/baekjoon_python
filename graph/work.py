# 작업,2056번
import sys
from collections import deque

def tsort():
    queue =deque()
    for node in range(1,n+1):
        if inDegree[node]==0:
            queue.append(node)
            dp[node]=time[node]
    while queue:
        q=queue.popleft()
        for adjNode in graph[q]:
            dp[adjNode]=max(dp[adjNode],dp[q]+time[adjNode])
            inDegree[adjNode]-=1
            if inDegree[adjNode]==0:
                queue.append(adjNode)

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
inDegree = [0]*(n+1)
time=[0]
dp = [0]*(n+1)

for curNode in range(1, n + 1):
    work = list(map(int,sys.stdin.readline().rstrip().split()))
    time.append(work[0])
    inDegree[curNode]=work[1]
    for preNode in work[2:]:
        graph[preNode].append(curNode)
tsort()
print(max(dp))