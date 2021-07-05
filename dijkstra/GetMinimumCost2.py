# 최소비용 구하기2, 11779번
import sys
import heapq
def dijkstra():
    heap = []
    dp[startNode]=0
    heapq.heappush(heap,(0,startNode))
    while heap:
        curCost,curNode = heapq.heappop(heap)
        if dp[curNode]<curCost :
            continue
        for adjNode,cost in graph[curNode]:
            if dp[adjNode]>curCost+cost:
                dp[adjNode] = curCost + cost
                path[adjNode]=curNode
                heapq.heappush(heap,(curCost + cost,adjNode))

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
dp = [float('INF') for _ in range(n+1)]
path = [i for i in range(n+1)]

for _ in range(m):
    cur, next, cost = map(int,sys.stdin.readline().rstrip().split())
    graph[cur].append([next,cost])
startNode, targetNode = map(int,sys.stdin.readline().rstrip().split())
dijkstra()

cnt=1
result=[targetNode]
curPathNode=targetNode
while not path[curPathNode]==curPathNode:
    curPathNode = path[curPathNode]
    result.append(curPathNode)
    cnt+=1
result.reverse()
print(dp[targetNode])
print(cnt)
print(*result)