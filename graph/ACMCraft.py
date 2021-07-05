# ACM Craft, 1005번
import sys
from collections import deque
def tSort():
    queue = deque()
    for node in range(1,n+1):
        if inDegree[node] == 0:
            queue.append(node)
            dp[node] = buildTime[node]
    while queue:
        curNode = queue.popleft()
        for adjNode in graph[curNode]:
            inDegree[adjNode] -= 1
            dp[adjNode]=max(dp[adjNode],dp[curNode]+buildTime[adjNode])
            if inDegree[adjNode] == 0:
                queue.append(adjNode)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().rstrip().split())
    dp=[0]*(n+1)
    inDegree=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    buildTime = [0]+ list(map(int,sys.stdin.readline().rstrip().split()))

    for _ in range(k):
        preNode, postNode = map(int, sys.stdin.readline().rstrip().split())
        graph[preNode].append(postNode)
        inDegree[postNode]+=1

    target = int(sys.stdin.readline().rstrip())
    tSort()
    print(dp[target])
