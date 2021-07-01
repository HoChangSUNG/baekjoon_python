# 문제집, 1766번
import sys
import heapq
def tsort():
    heap=[]
    for i in range(1,n+1):
        if inDegree[i]==0:
            heapq.heappush(heap,i)
    while heap:
        node = heapq.heappop(heap)
        print(node,end=' ')
        for adjNode in graph[node]:
            inDegree[adjNode]-=1
            if inDegree[adjNode]==0:
                heapq.heappush(heap,adjNode)

n,m = map(int, sys.stdin.readline().rstrip().split())
inDegree = [0]*(n+1)
graph=[[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    inDegree[b]+=1

tsort()