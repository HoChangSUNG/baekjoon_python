# 음악프로그램,2623번
import sys
from collections import deque
def tsort():
    queue=deque()
    for i in range(1,n+1):
        if inDegree[i]==0:
            queue.append(i)
    while queue:
        curNode = queue.popleft()
        result.append(curNode)
        for adjNode in graph[curNode]:
            inDegree[adjNode]-=1
            if inDegree[adjNode]==0:
                queue.append(adjNode)

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
inDegree=[0]*(n+1)
result = []
for _ in range(m):
    order = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(1,order[0]):
        graph[order[i]].append(order[i+1])
        inDegree[order[i+1]]+=1
tsort()
if len(result)==n:
    for node in result:
        print(node)
else:
    print(0)