# Strahler 순서, 9470번
import sys
from collections import deque
def tsort():
    queue= deque()
    for i in range(1,m+1):
        if inDegree[i]==0:
            strahlerOrder[i]=1
            queue.append(i)
    while queue:
        curNode = queue.popleft()
        for nextNode in graph[curNode]:
            inDegree[nextNode]-=1
            if strahlerOrder[nextNode]<strahlerOrder[curNode]:
                strahlerOrder[nextNode]=strahlerOrder[curNode]
                strahlerCount[nextNode]=1
            elif strahlerOrder[nextNode]==strahlerOrder[curNode]:
                strahlerCount[nextNode]+=1

            if inDegree[nextNode]==0:
                queue.append(nextNode)
                if strahlerCount[nextNode]>1:
                    strahlerOrder[nextNode]+=1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k,m,p = map(int,sys.stdin.readline().rstrip().split())
    inDegree = [0]*(m+1)
    strahlerOrder = [0]*(m+1)
    strahlerCount=[0]*(m+1)
    graph = [[]for _ in range(m+1)]
    for _ in range(p):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        inDegree[b]+=1
    tsort()
    print(k,strahlerOrder[m])