# 임계경로,1948번
import sys
from collections import deque
def tsort():
    cnt = 0
    queue=deque()
    queue.append(start)
    while queue:
        curNode = queue.popleft()
        for adjNode,time in graph[curNode]:
            if pathTime[adjNode]<time+pathTime[curNode]:
                pathTime[adjNode] = time + pathTime[curNode]
            inDegree[adjNode]-=1
            if inDegree[adjNode]==0:
                queue.append(adjNode)

    queue.append(target)
    while queue:
        curNode = queue.popleft()
        for adjNode, time in reverseGraph[curNode]:
            if pathTime[curNode]-pathTime[adjNode]==time:
                cnt +=1
                if visited[adjNode]==0:
                    queue.append(adjNode)
                    visited[adjNode] = 1
    print(pathTime[target])
    print(cnt)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[]for _ in range(n+1)]
inDegree = [0]*(n+1)
pathTime=[0]*(n+1)
reverseGraph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    cur,next,t=map(int,sys.stdin.readline().rstrip().split())
    graph[cur].append([next,t])
    reverseGraph[next].append([cur,t])
    inDegree[next]+=1

start,target = map(int,sys.stdin.readline().rstrip().split())
tsort()


